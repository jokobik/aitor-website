document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.querySelector('.menu-toggle');
    const mainMenu = document.getElementById('main-menu');
    const header = document.querySelector('header');

    function setMobileMenuState(isMobile) {
        if (mainMenu && header) {
            const headerHeight = header.offsetHeight;
            if (isMobile) {
                mainMenu.style.transform = `translateY(-${headerHeight}px)`;
                mainMenu.style.opacity = '0';
                mainMenu.style.top = `${headerHeight}px`;
                mainMenu.classList.remove('open-desktop');
                header.classList.remove('open-desktop');
                mainMenu.classList.remove('open'); // Asegurarse de que esté cerrado al pasar a móvil
                header.classList.remove('open');
            } else {
                mainMenu.style.transform = '';
                mainMenu.style.opacity = '';
                mainMenu.style.top = '';
                mainMenu.classList.add('open-desktop');
                header.classList.add('open-desktop');
                mainMenu.classList.add('open'); // Asegurarse de que esté abierto en escritorio
                header.classList.add('open');
            }
        }
    }

    // Establecer el estado inicial al cargar la página
    setMobileMenuState(window.innerWidth <= 800);

    // Escuchar los cambios de tamaño de la ventana
    window.addEventListener('resize', function() {
        setMobileMenuState(window.innerWidth <= 800);
    });

    if (menuToggle && mainMenu && header) {
        menuToggle.addEventListener('click', function() {
            if (window.innerWidth <= 800) {
                mainMenu.classList.toggle('open');
                header.classList.toggle('open');
                const headerHeight = header.offsetHeight;
                if (mainMenu.classList.contains('open')) {
                    mainMenu.style.transform = `translateY(0%)`;
                    mainMenu.style.opacity = '1';
                } else {
                    mainMenu.style.transform = `translateY(-${headerHeight}px)`;
                    mainMenu.style.opacity = '0';
                }
            }
        });
    }
});