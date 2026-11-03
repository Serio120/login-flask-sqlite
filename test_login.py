import os
import tempfile
import unittest
from contextlib import closing
from pathlib import Path

from werkzeug.security import check_password_hash, generate_password_hash

_TEST_DIR = tempfile.TemporaryDirectory()
os.environ["FLASK_SECRET_KEY"] = "test-only-secret-key"
os.environ["DATABASE_PATH"] = str(Path(_TEST_DIR.name) / "test.db")

from app import app, inicializar_base_de_datos  # noqa: E402
from conexion import obtener_conexion  # noqa: E402


class LoginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config.update(TESTING=True)

    def setUp(self):
        inicializar_base_de_datos()
        with closing(obtener_conexion()) as conexion:
            conexion.execute("DELETE FROM usuarios")
            conexion.execute(
                "INSERT INTO usuarios (username, password) VALUES (?, ?)",
                ("hashed-user", generate_password_hash("correct-password")),
            )
            conexion.execute(
                "INSERT INTO usuarios (username, password) VALUES (?, ?)",
                ("legacy-user", "legacy-password"),
            )
            conexion.commit()
        self.client = app.test_client()

    def test_valid_password_starts_session(self):
        response = self.client.post(
            "/login",
            data={"username": "hashed-user", "password": "correct-password"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers["Location"], "/bienvenido")
        with self.client.session_transaction() as session:
            self.assertEqual(session["usuario"], "hashed-user")

    def test_invalid_password_is_rejected(self):
        response = self.client.post(
            "/login",
            data={"username": "hashed-user", "password": "wrong-password"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("incorrectos", response.get_data(as_text=True))
        with self.client.session_transaction() as session:
            self.assertNotIn("usuario", session)

    def test_legacy_plaintext_password_is_migrated_after_login(self):
        response = self.client.post(
            "/login",
            data={"username": "legacy-user", "password": "legacy-password"},
        )
        self.assertEqual(response.status_code, 302)
        with closing(obtener_conexion()) as conexion:
            stored = conexion.execute(
                "SELECT password FROM usuarios WHERE username = ?",
                ("legacy-user",),
            ).fetchone()[0]
        self.assertNotEqual(stored, "legacy-password")
        self.assertTrue(check_password_hash(stored, "legacy-password"))

    def test_logout_clears_session(self):
        with self.client.session_transaction() as session:
            session["usuario"] = "hashed-user"
        response = self.client.get("/logout")
        self.assertEqual(response.status_code, 302)
        with self.client.session_transaction() as session:
            self.assertNotIn("usuario", session)


if __name__ == "__main__":
    unittest.main()
