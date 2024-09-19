<?php

    include 'conexion_be.php';    

    $nombre_completo = $_POST['nombre_completo'];
    $correo = $_POST['correo'];
    $usuario = $_POST['usuario'];
    $contrasena = $_POST['contrasena'];
    $puntos = 0;

    //Encriptando contraseña
    $contrasena = hash('sha512', $contrasena);

    $query = "INSERT INTO usuarios(nombre_completo, correo, usuario, contrasena, puntos)
              VALUES('$nombre_completo', '$correo', '$usuario', '$contrasena', '$puntos')";

    //verificar que no se repitan los correos
    $verificar_correo = mysqli_query($conexion, "SELECT * FROM usuarios WHERE correo='$correo' ");

    if(mysqli_num_rows($verificar_correo) > 0){
        echo '
            <script>
                alert("Este correo ya está registrado, intenta con otro diferente");
                window.location = "../index.php";
            </script>        
        ';
        exit();
    }

    //verificar que no se repitan los nombre de usuario 
    $verificar_usuario = mysqli_query($conexion, "SELECT * FROM usuarios WHERE usuario='$usuario' ");

    if(mysqli_num_rows($verificar_usuario) > 0){
        echo '
            <script>
                alert("Este usuario ya está registrado, intenta con otro diferente");
                window.location = "../index.php";
            </script>        
        ';
        exit();
    }
    
    $ejecutar = mysqli_query($conexion, $query);


    if($ejecutar){
        echo'
            <script>
                alert("Usuario almacenado exitosamente")
                window.location = "../index.php";
            </script>  
        ';
    }else{
        echo'
            <script>
                alert("Intentalo de nuevo, Usuario no almacenado")
                window.location = "../index.php";
            </script>  
        ';  
    }

    mysqli_close($conexion);
?>