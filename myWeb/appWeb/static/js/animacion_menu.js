document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.querySelector('.menu-toggle');
    const mainMenu = document.getElementById('main-menu');
    const header = document.querySelector('header');

    if (menuToggle && mainMenu && header) {
        // Función para verificar si estamos en modo móvil
        const isMobile = () => window.innerWidth <= 800;

        // Función para manejar los bordes SOLO en móvil
        const handleHeaderBorders = () => {
            if (!isMobile()) {
                // Reset completo en modo escritorio
                header.style.borderBottomLeftRadius = '';
                header.style.borderBottomRightRadius = '';
                return;
            }

            // Solo modificar bordes en móvil cuando el menú está abierto
            if (mainMenu.classList.contains('open')) {
                header.style.borderBottomLeftRadius = '0';
                header.style.borderBottomRightRadius = '0';
            } else {
                header.style.borderBottomLeftRadius = '10px';
                header.style.borderBottomRightRadius = '10px';
            }
        };

        // Inicialización del menú
        function initMenu() {
            if (isMobile()) {
                // Configuración inicial para móvil
                mainMenu.style.transition = 'none';
                header.style.transition = 'none';
                mainMenu.classList.remove('open');
                handleHeaderBorders();
                setTimeout(() => {
                    mainMenu.style.transition = '';
                    header.style.transition = '';
                }, 10);
            } else {
                // Reset completo para escritorio
                mainMenu.style.transition = '';
                header.style.transition = '';
                mainMenu.classList.remove('open');
                handleHeaderBorders();
            }
        }

        // Manejo del clic del botón (solo en móvil)
        menuToggle.addEventListener('click', function() {
            if (!isMobile()) return;

            mainMenu.classList.toggle('open');
            handleHeaderBorders();
        });

        // Escuchar cambios de tamaño
        window.addEventListener('resize', initMenu);

        // Inicializar
        initMenu();
    }
});