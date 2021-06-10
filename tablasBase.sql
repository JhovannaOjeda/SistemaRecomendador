USE [MoviesHub]
GO

/****** Object:  Table [dbo].[auth_group]    Script Date: 6/9/2021 5:45:30 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[auth_group](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[name] [nvarchar](80) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
UNIQUE NONCLUSTERED 
(
	[name] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[auth_group_permissions](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[group_id] [int] NOT NULL,
	[permission_id] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
 CONSTRAINT [auth_group_permissions_group_id_permission_id_0cd325b0_uniq] UNIQUE NONCLUSTERED 
(
	[group_id] ASC,
	[permission_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[auth_group_permissions]  WITH CHECK ADD  CONSTRAINT [auth_group_permissions_group_id_b120cbf9_fk_auth_group_id] FOREIGN KEY([group_id])
REFERENCES [dbo].[auth_group] ([id])
GO

ALTER TABLE [dbo].[auth_group_permissions] CHECK CONSTRAINT [auth_group_permissions_group_id_b120cbf9_fk_auth_group_id]
GO

ALTER TABLE [dbo].[auth_group_permissions]  WITH CHECK ADD  CONSTRAINT [auth_group_permissions_permission_id_84c5c92e_fk_auth_permission_id] FOREIGN KEY([permission_id])
REFERENCES [dbo].[auth_permission] ([id])
GO

ALTER TABLE [dbo].[auth_group_permissions] CHECK CONSTRAINT [auth_group_permissions_permission_id_84c5c92e_fk_auth_permission_id]
GO

CREATE TABLE [dbo].[auth_permission](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[name] [nvarchar](255) NOT NULL,
	[content_type_id] [int] NOT NULL,
	[codename] [nvarchar](100) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
 CONSTRAINT [auth_permission_content_type_id_codename_01ab375a_uniq] UNIQUE NONCLUSTERED 
(
	[content_type_id] ASC,
	[codename] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[auth_permission]  WITH CHECK ADD  CONSTRAINT [auth_permission_content_type_id_2f476e4b_fk_django_content_type_id] FOREIGN KEY([content_type_id])
REFERENCES [dbo].[django_content_type] ([id])
GO

ALTER TABLE [dbo].[auth_permission] CHECK CONSTRAINT [auth_permission_content_type_id_2f476e4b_fk_django_content_type_id]
GO

CREATE TABLE [dbo].[django_admin_log](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[action_time] [datetime2](7) NOT NULL,
	[object_id] [nvarchar](max) NULL,
	[object_repr] [nvarchar](200) NOT NULL,
	[action_flag] [smallint] NOT NULL,
	[change_message] [nvarchar](max) NOT NULL,
	[content_type_id] [int] NULL,
	[user_id] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

ALTER TABLE [dbo].[django_admin_log]  WITH CHECK ADD  CONSTRAINT [django_admin_log_content_type_id_c4bce8eb_fk_django_content_type_id] FOREIGN KEY([content_type_id])
REFERENCES [dbo].[django_content_type] ([id])
GO

ALTER TABLE [dbo].[django_admin_log] CHECK CONSTRAINT [django_admin_log_content_type_id_c4bce8eb_fk_django_content_type_id]
GO

ALTER TABLE [dbo].[django_admin_log]  WITH CHECK ADD  CONSTRAINT [django_admin_log_user_id_c564eba6_fk_Usuarios_user_id] FOREIGN KEY([user_id])
REFERENCES [dbo].[Usuarios_user] ([id])
GO

ALTER TABLE [dbo].[django_admin_log] CHECK CONSTRAINT [django_admin_log_user_id_c564eba6_fk_Usuarios_user_id]
GO

ALTER TABLE [dbo].[django_admin_log]  WITH CHECK ADD  CONSTRAINT [django_admin_log_action_flag_a8637d59_check] CHECK  (([action_flag]>=(0)))
GO

ALTER TABLE [dbo].[django_admin_log] CHECK CONSTRAINT [django_admin_log_action_flag_a8637d59_check]
GO

CREATE TABLE [dbo].[django_content_type](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[app_label] [nvarchar](100) NOT NULL,
	[model] [nvarchar](100) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
 CONSTRAINT [django_content_type_app_label_model_76bd3d3b_uniq] UNIQUE NONCLUSTERED 
(
	[app_label] ASC,
	[model] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
CREATE TABLE [dbo].[django_migrations](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[app] [nvarchar](255) NOT NULL,
	[name] [nvarchar](255) NOT NULL,
	[applied] [datetime2](7) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[django_session](
	[session_key] [nvarchar](40) NOT NULL,
	[session_data] [nvarchar](max) NOT NULL,
	[expire_date] [datetime2](7) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[session_key] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

CREATE TABLE [dbo].[home_suscriptor](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[name] [nvarchar](50) NOT NULL,
	[lastname] [nvarchar](50) NOT NULL,
	[username] [nvarchar](50) NOT NULL,
	[email] [nvarchar](200) NOT NULL,
	[password] [nvarchar](50) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[Usuarios_suscriptor](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[nombre] [nvarchar](50) NOT NULL,
	[apellidos] [nvarchar](50) NOT NULL,
	[nombreUser] [nvarchar](50) NOT NULL,
	[correo] [nvarchar](200) NOT NULL,
	[contraseña] [nvarchar](50) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[Usuarios_user](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[password] [nvarchar](128) NOT NULL,
	[last_login] [datetime2](7) NULL,
	[is_superuser] [bit] NOT NULL,
	[username] [nvarchar](150) NOT NULL,
	[first_name] [nvarchar](30) NOT NULL,
	[last_name] [nvarchar](150) NOT NULL,
	[email] [nvarchar](254) NOT NULL,
	[is_staff] [bit] NOT NULL,
	[is_active] [bit] NOT NULL,
	[date_joined] [datetime2](7) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
UNIQUE NONCLUSTERED 
(
	[username] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[Usuarios_user_groups](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[user_id] [int] NOT NULL,
	[group_id] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
 CONSTRAINT [Usuarios_user_groups_user_id_group_id_d99064c4_uniq] UNIQUE NONCLUSTERED 
(
	[user_id] ASC,
	[group_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[Usuarios_user_groups]  WITH CHECK ADD  CONSTRAINT [Usuarios_user_groups_group_id_c88bca9d_fk_auth_group_id] FOREIGN KEY([group_id])
REFERENCES [dbo].[auth_group] ([id])
GO

ALTER TABLE [dbo].[Usuarios_user_groups] CHECK CONSTRAINT [Usuarios_user_groups_group_id_c88bca9d_fk_auth_group_id]
GO

ALTER TABLE [dbo].[Usuarios_user_groups]  WITH CHECK ADD  CONSTRAINT [Usuarios_user_groups_user_id_1274a848_fk_Usuarios_user_id] FOREIGN KEY([user_id])
REFERENCES [dbo].[Usuarios_user] ([id])
GO

ALTER TABLE [dbo].[Usuarios_user_groups] CHECK CONSTRAINT [Usuarios_user_groups_user_id_1274a848_fk_Usuarios_user_id]
GO

CREATE TABLE [dbo].[Usuarios_user_user_permissions](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[user_id] [int] NOT NULL,
	[permission_id] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
 CONSTRAINT [Usuarios_user_user_permissions_user_id_permission_id_fefe60b1_uniq] UNIQUE NONCLUSTERED 
(
	[user_id] ASC,
	[permission_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[Usuarios_user_user_permissions]  WITH CHECK ADD  CONSTRAINT [Usuarios_user_user_permissions_permission_id_f5746574_fk_auth_permission_id] FOREIGN KEY([permission_id])
REFERENCES [dbo].[auth_permission] ([id])
GO

ALTER TABLE [dbo].[Usuarios_user_user_permissions] CHECK CONSTRAINT [Usuarios_user_user_permissions_permission_id_f5746574_fk_auth_permission_id]
GO

ALTER TABLE [dbo].[Usuarios_user_user_permissions]  WITH CHECK ADD  CONSTRAINT [Usuarios_user_user_permissions_user_id_7e374165_fk_Usuarios_user_id] FOREIGN KEY([user_id])
REFERENCES [dbo].[Usuarios_user] ([id])
GO

ALTER TABLE [dbo].[Usuarios_user_user_permissions] CHECK CONSTRAINT [Usuarios_user_user_permissions_user_id_7e374165_fk_Usuarios_user_id]
GO


