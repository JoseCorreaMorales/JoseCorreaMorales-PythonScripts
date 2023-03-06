<?php
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "myDB";

// Crear la conexión
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar la conexión
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Obtener los datos del formulario
$username = $_POST["username"];
$password = $_POST["password"];

// Ejecutar la consulta SQL para insertar los datos en la tabla correspondiente
$sql = "INSERT INTO login (username, password) VALUES ('$username', '$password')";

if ($conn->query($sql) === TRUE) {
    echo "Datos guardados correctamente";
} else {
    echo "Error al guardar los datos: " . $conn->error;
}

// Cerrar la conexión
$conn->close();
?>