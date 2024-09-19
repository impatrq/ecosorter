<?php
    session_start();

    if(!isset($_SESSION['usuario'])){
        echo '
            <script>
                alert("Por favor, Iniciar Sesión");
            </script>
        ';
        header("location: index.php");
        session_destroy();
        die();
    }

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tus Puntos - Ecosorter</title>
    <link rel="stylesheet" href="assets/css/estilos_puntos.css">
</head>
<body>
    <header>
        <div class="cabeza">
            <img src="assets/images/whatsapp-20image-202024-04-09-20at-2008.27.25.png" alt width="65" class="logo">
            <h1>Ecosorter</h1>
        </div>
        <a href="php/cerrar_sesion.php" class="centro">Cerrar sesión</a>
    </header>
    
    <main>
        <h2 class="bienvenido">Bienvenido <?php echo $_SESSION['usuario']; ?>, estos son tus puntos:</h2>
        <div class="puntos"> <?php echo $_SESSION['puntos']; ?> </div>
        <form action="catalogo.php" method="POST" class="catalogo">
            <button> Ver Catálogo </button>
        </form> 
    </main>

    <footer>
        <div class="sponsors">
            <h3>Sponsors</h3>
            <div class="imagenes">
                <img src="assets/images/imagen_2024-08-07_105342505.png"  class="sponsors_imagen" width= "15%">
                <img src="assets/images/imagen_2024-08-23_110759560.png"  class="sponsors_imagen" width= "15%">
                <img src="assets/images/imagen_2024-09-09_143903477.png"  class="sponsors_imagen" width= "15%">
                <img src="assets/images/imagen_2024-09-09_144135045.png"  class="sponsors_imagen" width= "15%">
            </div>
        </div>


        <div class="contacto">
            <h3>Contactanos</h3>
            <ul>
                <li>Instagram: <a href="https://www.instagram.com/proyecto_ecosorter24/">proyecto_ecosorter24</a></li>
                <li>Email: <a href="mailto:ecosorterimpa2024@gmail.com">ecosorterimpa2024@gmail.com</a></li>
            </ul>

        </div>
    </footer>
    

</body>
</html>