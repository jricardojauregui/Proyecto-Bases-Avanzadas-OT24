-- inserta usuario

DELIMITER //
CREATE PROCEDURE InsertUsuario(
    IN p_username VARCHAR(100),
    IN p_clave VARCHAR(100),
    IN p_nom_usr VARCHAR(100),
    IN p_apellido_usr VARCHAR(100),
    IN p_correo_usr VARCHAR(100),
    IN p_tel_usr VARCHAR(100),
    IN p_tel_domicilio VARCHAR(100),
    IN p_direccion VARCHAR(100),
    IN p_foto_usuario VARCHAR(255)
)
BEGIN
    INSERT INTO usuarios (
        username, clave, nom_usr, apellido_usr, correo_usr, tel_usr, tel_domicilio, direccion, foto_usuario
    ) 
    VALUES (
        p_username, p_clave, p_nom_usr, p_apellido_usr, p_correo_usr, p_tel_usr, p_tel_domicilio, p_direccion, p_foto_usuario
    );
END //
DELIMITER ;

-- Actualizar un usuario 
DELIMITER //
CREATE PROCEDURE UpdateUsuario(
    IN p_username VARCHAR(100),
    IN p_clave VARCHAR(100),
    IN p_nom_usr VARCHAR(100),
    IN p_apellido_usr VARCHAR(100),
    IN p_correo_usr VARCHAR(100),
    IN p_tel_usr VARCHAR(100),
    IN p_tel_domicilio VARCHAR(100),
    IN p_direccion VARCHAR(100),
    IN p_foto_usuario VARCHAR(255)
)
BEGIN
    UPDATE usuarios
    SET 
        username = p_username
        clave = p_clave,
        nom_usr = p_nom_usr,
        apellido_usr = p_apellido_usr,
        correo_usr = p_correo_usr,
        tel_usr = p_tel_usr,
        tel_domicilio = p_tel_domicilio,
        direccion = p_direccion,
        foto_usuario = p_foto_usuario
    WHERE 
        id_usr = p_id_usr;
END //
DELIMITER ;

-- delete usuario
DELIMITER //
CREATE PROCEDURE DeleteUsuario(
    IN p_id_usr INT
)
BEGIN
    DELETE FROM usuarios
    WHERE id_usr = p_id_usr;
END //
DELIMITER ;

-- Mostrar todos los usuarios
DELIMITER //
CREATE PROCEDURE MostrarUsuarios()
BEGIN
    SELECT 
        id_usr, clave, nom_usr, apellido_usr, correo_usr, tel_usr, tel_domicilio, direccion, fecha_registro, foto_usuario
    FROM 
        usuarios;
END //
DELIMITER ;

-- Mostrar un usuario por ID
DELIMITER //
CREATE PROCEDURE MostrarUsuarioPorID(
    IN p_id_usr INT
)
BEGIN
    SELECT 
        id_usr, clave, nom_usr, apellido_usr, correo_usr, tel_usr, tel_domicilio, direccion, fecha_registro, foto_usuario
    FROM 
        usuarios
    WHERE 
        id_usr = p_id_usr;
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE MostrarUsuarioPorID(
    IN p_nombre_usr INT
)
BEGIN
    SELECT 
        id_usr, clave, nom_usr, apellido_usr, correo_usr, tel_usr, tel_domicilio, direccion, fecha_registro, foto_usuario
    FROM 
        usuarios
    WHERE 
        nom_usr = p_nombre_usr;
END //
DELIMITER ;