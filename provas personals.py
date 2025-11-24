<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema de Login Multiidioma</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .container {
            background: white;
            border-radius: 15px;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
            width: 100%;
            max-width: 400px;
            padding: 40px;
            animation: slideIn 0.5s ease;
        }

        @keyframes slideIn {
            from { opacity: 0; transform: translateY(-30px); }
            to   { opacity: 1; transform: translateY(0); }
        }

        .language-selector {
            display: flex;
            justify-content: flex-end;
            gap: 10px;
            margin-bottom: 30px;
        }

        .lang-btn {
            background: transparent;
            border: 2px solid #667eea;
            color: #667eea;
            padding: 5px 15px;
            border-radius: 20px;
            cursor: pointer;
            font-weight: bold;
            transition: 0.3s ease;
            font-size: 12px;
        }

        .lang-btn:hover {
            background: #667eea;
            color: white;
            transform: scale(1.05);
        }

        .lang-btn.active {
            background: #667eea;
            color: white;
        }

        .header {
            text-align: center;
            margin-bottom: 30px;
        }

        .header h1 {
            color: #333;
            font-size: 28px;
            margin-bottom: 10px;
        }

        .header p {
            color: #666;
            font-size: 14px;
        }

        .login-form {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .form-group label {
            color: #333;
            font-weight: 600;
            font-size: 14px;
        }

        .form-group input {
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 14px;
            transition: 0.3s ease;
        }

        .form-group input:focus {
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
            outline: none;
        }

        .btn-login {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 14px;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: 0.3s ease;
        }

        .btn-login:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }

        .dashboard {
            display: none;
            text-align: center;
        }

        .dashboard.active { display: block; }

        .user-info {
            background: #f5f5f5;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }

        .btn-logout {
            background: #ff4757;
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 8px;
            font-size: 14px;
            cursor: pointer;
            transition: 0.3s ease;
        }

        .btn-logout:hover {
            background: #ff3838;
            transform: translateY(-2px);
        }

        .error-message {
            color: #ff4757;
            font-size: 14px;
            text-align: center;
            margin-top: 10px;
            display: none;
        }

        .error-message.show {
            display: block;
            animation: shake 0.5s ease;
        }

        @keyframes shake {
            0%, 100% { transform: translateX(0); }
            25% { transform: translateX(-10px); }
            75% { transform: translateX(10px); }
        }

        .flags { font-size: 18px; }
    </style>
</head>
<body>

<div class="container">

    <!-- Selector de Idioma -->
    <div class="language-selector">
        <button class="lang-btn active" data-lang="es"><span class="flags">🇪🇸</span> ES</button>
        <button class="lang-btn" data-lang="en"><span class="flags">🇬🇧</span> EN</button>
        <button class="lang-btn" data-lang="de"><span class="flags">🇩🇪</span> DE</button>
    </div>

    <!-- LOGIN -->
    <div id="loginSection">
        <div class="header">
            <h1 data-translate="title">Sistema de Inicio de Sesión</h1>
            <p data-translate="subtitle">Ingresa tus credenciales para continuar</p>
        </div>

        <form id="loginForm" class="login-form">
            <div class="form-group">
                <label data-translate="username">Usuario</label>
                <input type="text" id="username" required>
            </div>

            <div class="form-group">
                <label data-translate="password">Contraseña</label>
                <input type="password" id="password" required>
            </div>

            <button class="btn-login" type="submit" data-translate="loginBtn">Iniciar Sesión</button>

            <div class="error-message" id="errorMessage" data-translate="error"></div>
        </form>
    </div>

    <!-- DASHBOARD -->
    <div id="dashboardSection" class="dashboard">
        <div class="welcome-message">
            <h2 data-translate="welcomeTitle">¡Bienvenido!</h2>
            <p data-translate="welcomeMsg">Has iniciado sesión exitosamente</p>
        </div>

        <div class="user-info">
            <p><strong data-translate="userLabel">Usuario:</strong> <span id="displayUsername"></span></p>
            <p><strong data-translate="statusLabel">Estado:</strong> <span data-translate="statusActive">Activo</span></p>
        </div>

        <button id="logoutBtn" class="btn-logout" data-translate="logoutBtn">Cerrar Sesión</button>
    </div>

</div>

<script>
    const translations = {
        es: {
            title: "Sistema de Inicio de Sesión",
            subtitle: "Ingresa tus credenciales para continuar",
            username: "Usuario",
            password: "Contraseña",
            loginBtn: "Iniciar Sesión",
            error: "Usuario o contraseña incorrectos",
            welcomeTitle: "¡Bienvenido!",
            welcomeMsg: "Has iniciado sesión exitosamente",
            userLabel: "Usuario:",
            statusLabel: "Estado:",
            statusActive: "Activo",
            logoutBtn: "Cerrar Sesión"
        },
        en: {
            title: "Login System",
            subtitle: "Enter your credentials to continue",
            username: "Username",
            password: "Password",
            loginBtn: "Login",
            error: "Incorrect username or password",
            welcomeTitle: "Welcome!",
            welcomeMsg: "You have successfully logged in",
            userLabel: "User:",
            statusLabel: "Status:",
            statusActive: "Active",
            logoutBtn: "Logout"
        },
        de: {
            title: "Anmeldesystem",
            subtitle: "Geben Sie Ihre Zugangsdaten ein, um fortzufahren",
            username: "Benutzername",
            password: "Passwort",
            loginBtn: "Anmelden",
            error: "Falscher Benutzername oder Passwort",
            welcomeTitle: "Willkommen!",
            welcomeMsg: "Sie haben sich erfolgreich angemeldet",
            userLabel: "Benutzer:",
            statusLabel: "Status:",
            statusActive: "Aktiv",
            logoutBtn: "Abmelden"
        }
    };

    const users = [
        { username: 'admin', password: 'admin123' },
        { username: 'user', password: 'user123' },
        { username: 'demo', password: 'demo123' }
    ];

    let currentLanguage = "es";

    function changeLanguage(lang) {
        currentLanguage = lang;
        document.documentElement.lang = lang;

        document.querySelectorAll("[data-translate]").forEach(el => {
            const key = el.getAttribute("data-translate");
            el.textContent = translations[lang][key];
        });

        document.querySelectorAll(".lang-btn").forEach(btn => {
            btn.classList.toggle("active", btn.dataset.lang === lang);
        });
    }

    document.querySelectorAll(".lang-btn").forEach(btn => {
        btn.onclick = () => changeLanguage(btn.dataset.lang);
    });

    const loginForm = document.getElementById("loginForm");
    const loginSection = document.getElementById("loginSection");
    const dashboardSection = document.getElementById("dashboardSection");
    const errorMessage = document.getElementById("errorMessage");

    loginForm.onsubmit = (e) => {
        e.preventDefault();
        const u = username.value;
        const p = password.value;

        const user = users.find(x => x.username === u && x.password === p);

        if (!user) {
            errorMessage.classList.add("show");
            setTimeout(() => errorMessage.classList.remove("show"), 3000);
            return;
        }

        sessionStorage.setItem("loggedUser", u);
        displayUsername.textContent = u;
        loginSection.style.display = "none";
        dashboardSection.classList.add("active");
    };

    logoutBtn.onclick = () => {
        sessionStorage.removeItem("loggedUser");
        dashboardSection.classList.remove("
