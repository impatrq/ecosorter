<?php
session_start();
include 'conexion_be.php';

// Verificar si el usuario ha iniciado sesión
if (isset($_SESSION['usuario']) && isset($_SESSION['puntos'])) {
    $correo = $_SESSION['usuario'];
    $puntos = $_SESSION['puntos'];

    // Actualizar los puntos del usuario en la base de datos antes de destruir la sesión
    $actualizar_puntos = mysqli_query($conexion, "UPDATE usuarios SET puntos='$puntos' WHERE correo='$correo'");

    if ($actualizar_puntos) {
        // Destruir la sesión después de guardar los puntos
        session_destroy();
        header("location: ../index.php");
        exit;
    } else {
        echo '<script>alert("Error al guardar los puntos. Por favor, intenta nuevamente.");</script>';
    }
} else {
    // Si no hay sesión activa, redirigir directamente
    header("location: ../index.php");
    exit;
}
?>
