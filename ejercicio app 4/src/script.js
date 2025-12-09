// ==========================================
// ELEMENTOS DEL DOM
// ==========================================

// Botones principales
const homeBtn = document.getElementById('homeBtn');
const menuBtn = document.getElementById('menuBtn');
const searchBtn = document.getElementById('searchBtn');
const userBtn = document.getElementById('userBtn');
const cartBtn = document.getElementById('cartBtn');
const notificationBtn = document.getElementById('notificationBtn');
const settingsBtn = document.getElementById('settingsBtn');
const chatBtn = document.getElementById('chatBtn');

// Elementos de la UI
const sideMenu = document.getElementById('sideMenu');
const searchBar = document.getElementById('searchBar');
const overlay = document.getElementById('overlay');

// Paneles
const userPanel = document.getElementById('userPanel');
const cartPanel = document.getElementById('cartPanel');
const notificationsPanel = document.getElementById('notificationsPanel');
const settingsPanel = document.getElementById('settingsPanel');
const chatWindow = document.getElementById('chatWindow');

// Botones de cierre
const closeMenuBtn = document.getElementById('closeMenuBtn');
const closeSearchBtn = document.getElementById('closeSearchBtn');
const closeUserBtn = document.getElementById('closeUserBtn');
const closeCartBtn = document.getElementById('closeCartBtn');
const closeNotificationsBtn = document.getElementById('closeNotificationsBtn');
const closeSettingsBtn = document.getElementById('closeSettingsBtn');
const closeChatBtn = document.getElementById('closeChatBtn');

// Otros elementos
const authOptions = document.getElementById('authOptions');
const userInfo = document.getElementById('userInfo');
const loginBtn = document.getElementById('loginBtn');
const registerBtn = document.getElementById('registerBtn');
const logoutBtn = document.getElementById('logoutBtn');
const darkModeToggle = document.getElementById('darkModeToggle');
const markAllReadBtn = document.getElementById('markAllReadBtn');
const chatInput = document.getElementById('chatInput');
const sendMessageBtn = document.getElementById('sendMessageBtn');
const cartBadge = document.getElementById('cartBadge');
const notificationBadge = document.getElementById('notificationBadge');

// ==========================================
// ESTADO DE LA APLICACIÓN
// ==========================================

let isUserAuthenticated = false;
let cartItemCount = 3;
let unreadNotifications = 5;

// ==========================================
// FUNCIONES AUXILIARES
// ==========================================

// Cerrar todos los paneles y menús
function closeAll() {
    sideMenu.classList.remove('active');
    searchBar.classList.remove('active');
    userPanel.classList.remove('active');
    cartPanel.classList.remove('active');
    notificationsPanel.classList.remove('active');
    settingsPanel.classList.remove('active');
    chatWindow.classList.remove('active');
    overlay.classList.remove('active');
}

// Abrir overlay
function openOverlay() {
    overlay.classList.add('active');
}

// Cerrar overlay
function closeOverlay() {
    overlay.classList.remove('active');
}

// Toggle (abrir/cerrar) un elemento
function toggleElement(element) {
    const isActive = element.classList.contains('active');
    closeAll();
    
    if (!isActive) {
        element.classList.add('active');
        if (element !== chatWindow) {
            openOverlay();
        }
    }
}

// ==========================================
// 1. BOTÓN HOME
// ==========================================

homeBtn.addEventListener('click', () => {
    closeAll();
    window.scrollTo({ top: 0, behavior: 'smooth' });
    // Aquí podrías cargar la página principal con fetch o cambiar de ruta
    console.log('Navegando a la página principal');
});

// ==========================================
// 2. MENÚ HAMBURGUESA
// ==========================================

menuBtn.addEventListener('click', () => {
    toggleElement(sideMenu);
});

closeMenuBtn.addEventListener('click', () => {
    closeAll();
});

// ==========================================
// 3. BÚSQUEDA
// ==========================================

searchBtn.addEventListener('click', () => {
    const isActive = searchBar.classList.contains('active');
    
    if (!isActive) {
        closeAll();
        searchBar.classList.add('active');
        document.getElementById('searchInput').focus();
    } else {
        searchBar.classList.remove('active');
    }
});

closeSearchBtn.addEventListener('click', () => {
    searchBar.classList.remove('active');
});

// Búsqueda al presionar Enter
document.getElementById('searchInput').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        const searchTerm = e.target.value;
        console.log('Buscando:', searchTerm);
        // Aquí implementarías la lógica de búsqueda
        alert(`Buscando: ${searchTerm}`);
    }
});

// ==========================================
// 4. USUARIO / CUENTA
// ==========================================

userBtn.addEventListener('click', () => {
    toggleElement(userPanel);
});

closeUserBtn.addEventListener('click', () => {
    closeAll();
});

// Login
loginBtn.addEventListener('click', () => {
    console.log('Iniciando sesión...');
    // Simulación de login exitoso
    isUserAuthenticated = true;
    authOptions.style.display = 'none';
    userInfo.style.display = 'block';
    alert('¡Sesión iniciada correctamente!');
});

// Registro
registerBtn.addEventListener('click', () => {
    console.log('Abriendo formulario de registro...');
    alert('Aquí se abriría el formulario de registro');
});

// Logout
logoutBtn.addEventListener('click', () => {
    console.log('Cerrando sesión...');
    isUserAuthenticated = false;
    authOptions.style.display = 'flex';
    userInfo.style.display = 'none';
    closeAll();
    alert('Has cerrado sesión');
});

// ==========================================
// 5. CARRITO
// ==========================================

cartBtn.addEventListener('click', () => {
    toggleElement(cartPanel);
});

closeCartBtn.addEventListener('click', () => {
    closeAll();
});

// Eliminar items del carrito
document.querySelectorAll('.remove-item').forEach(btn => {
    btn.addEventListener('click', (e) => {
        const cartItem = e.target.closest('.cart-item');
        cartItem.remove();
        
        cartItemCount--;
        updateCartBadge();
        
        // Si no hay más items, mostrar carrito vacío
        const cartItems = document.getElementById('cartItems');
        if (cartItems.children.length === 0) {
            cartItems.style.display = 'none';
            document.getElementById('emptyCart').style.display = 'block';
            document.getElementById('cartSummary').style.display = 'none';
        }
    });
});

// Actualizar badge del carrito
function updateCartBadge() {
    if (cartItemCount > 0) {
        cartBadge.textContent = cartItemCount;
        cartBadge.style.display = 'block';
    } else {
        cartBadge.style.display = 'none';
    }
}

// ==========================================
// 6. NOTIFICACIONES
// ==========================================

notificationBtn.addEventListener('click', () => {
    toggleElement(notificationsPanel);
    
    // Marcar notificaciones como leídas después de 1 segundo
    setTimeout(() => {
        markNotificationsAsRead();
    }, 1000);
});

closeNotificationsBtn.addEventListener('click', () => {
    closeAll();
});

// Marcar todas como leídas
markAllReadBtn.addEventListener('click', () => {
    markNotificationsAsRead();
    alert('Todas las notificaciones han sido marcadas como leídas');
});

// Función para marcar notificaciones como leídas
function markNotificationsAsRead() {
    const unreadNotifs = document.querySelectorAll('.notification-item.unread');
    unreadNotifs.forEach(notif => {
        notif.classList.remove('unread');
    });
    
    unreadNotifications = 0;
    updateNotificationBadge();
}

// Actualizar badge de notificaciones
function updateNotificationBadge() {
    if (unreadNotifications > 0) {
        notificationBadge.textContent = unreadNotifications;
        notificationBadge.style.display = 'block';
    } else {
        notificationBadge.style.display = 'none';
    }
}

// ==========================================
// 7. CONFIGURACIÓN
// ==========================================

settingsBtn.addEventListener('click', () => {
    toggleElement(settingsPanel);
});

closeSettingsBtn.addEventListener('click', () => {
    closeAll();
});

// Modo oscuro
darkModeToggle.addEventListener('change', (e) => {
    if (e.target.checked) {
        document.body.classList.add('dark-mode');
        localStorage.setItem('darkMode', 'enabled');
    } else {
        document.body.classList.remove('dark-mode');
        localStorage.setItem('darkMode', 'disabled');
    }
});

// Cargar preferencia de modo oscuro
if (localStorage.getItem('darkMode') === 'enabled') {
    document.body.classList.add('dark-mode');
    darkModeToggle.checked = true;
}

// ==========================================
// 8. REDES SOCIALES
// ==========================================

// Los enlaces ya están configurados en el HTML con target="_blank"
// Se abrirán automáticamente en nueva pestaña

document.querySelectorAll('.social-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
        console.log('Abriendo red social:', e.currentTarget.href);
    });
});

// ==========================================
// 9. CHAT DE SOPORTE
// ==========================================

chatBtn.addEventListener('click', () => {
    const isActive = chatWindow.classList.contains('active');
    
    if (!isActive) {
        closeAll();
        chatWindow.classList.add('active');
    } else {
        chatWindow.classList.remove('active');
    }
});

closeChatBtn.addEventListener('click', () => {
    chatWindow.classList.remove('active');
});

// Enviar mensaje
function sendMessage() {
    const message = chatInput.value.trim();
    
    if (message !== '') {
        // Crear mensaje del usuario
        const chatMessages = document.getElementById('chatMessages');
        const messageDiv = document.createElement('div');
        messageDiv.className = 'message user-message';
        messageDiv.innerHTML = `
            <div class="message-avatar">
                <i class="fas fa-user"></i>
            </div>
            <div class="message-content">
                <p>${message}</p>
                <span class="message-time">Ahora</span>
            </div>
        `;
        
        chatMessages.appendChild(messageDiv);
        chatInput.value = '';
        
        // Scroll al final
        chatMessages.scrollTop = chatMessages.scrollHeight;
        
        // Simular respuesta del bot después de 1 segundo
        setTimeout(() => {
            const botResponse = document.createElement('div');
            botResponse.className = 'message bot-message';
            botResponse.innerHTML = `
                <div class="message-avatar">
                    <i class="fas fa-robot"></i>
                </div>
                <div class="message-content">
                    <p>Gracias por tu mensaje. Un agente te responderá pronto. 😊</p>
                    <span class="message-time">Ahora</span>
                </div>
            `;
            
            chatMessages.appendChild(botResponse);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }, 1000);
    }
}

sendMessageBtn.addEventListener('click', sendMessage);

chatInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

// ==========================================
// 10. CERRAR CON OVERLAY
// ==========================================

overlay.addEventListener('click', () => {
    closeAll();
});

// ==========================================
// CERRAR CON TECLA ESC
// ==========================================

document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        closeAll();
    }
});

// ==========================================
// INICIALIZACIÓN
// ==========================================

console.log('✅ App iniciada correctamente');
console.log('💡 Presiona ESC para cerrar cualquier panel');