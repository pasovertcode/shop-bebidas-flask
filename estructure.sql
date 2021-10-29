CREATE TABLE usuarios (
    id_usuario BIGINT primary key AUTOINCREMENT,
    tipo_usuario int not null,
    username varchar(50) unique not null,
    password_hash varchar(255) not null,
    fecha_creacion_usuario DATETIME not null,
    estado_usuario varchar(50) not null default activo,
    email_usuario varchar(255) not null default [example@example.com]
);

CREATE TABLE productos (
    id_producto BIGINT PRIMARY KEY AUTOINCREMENT,
    nombre_producto VARCHAR (50)  NOT NULL,
    codigo_producto VARCHAR (50)  UNIQUE NOT NULL,
    info_producto   VARCHAR (255) NOT NULL,
    precio_producto INT           NOT NULL,
    estado_producto VARCHAR (20)  NOT NULL DEFAULT active
);

CREATE TABLE ventas (
    id_venta              INTEGER       PRIMARY KEY AUTOINCREMENT,
    codigo_venta          VARCHAR (255) NOT NULL,
    metodo_pago_venta     VARCHAR (255) NOT NULL,
    codigo_producto_venta VARCHAR (255) REFERENCES productos (codigo_producto) 
                                        NOT NULL,
    usuario_venta         VARCHAR (255) REFERENCES usuarios (username) 
                                        NOT NULL
);
CREATE TABLE wishlist (
    id_wishlist     INTEGER       PRIMARY KEY AUTOINCREMENT,
    codigo_producto VARCHAR (255) REFERENCES productos (codigo_producto) 
                                  NOT NULL,
    usuario         VARCHAR (255) REFERENCES usuarios (username) 
                                  NOT NULL
);
CREATE TABLE comentarios (
    id_comentario INTEGER PRIMARY KEY AUTOINCREMENT,
    id_venta      INTEGER REFERENCES ventas (id_venta),
    valoracion    INT     NOT NULL
                          DEFAULT (0) 
);
CREATE TABLE Log_Action_User (
    id_log      INTEGER       PRIMARY KEY AUTOINCREMENT
                              NOT NULL,
    username    VARCHAR (255) REFERENCES usuarios (username) 
                              NOT NULL,
    action_log  VARCHAR (255) NOT NULL,
    fecha_hora  DATETIME      NOT NULL,
    details_log TEXT          NOT NULL
);
