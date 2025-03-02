// Variables para el control del juego
let puntos = 0;               // Almacena los puntos actuales
let aciertosConsecutivos = 0;  // Cuenta los aciertos consecutivos
let totalPartidas = 0;        // Cuenta las partidas totales
let partidasGanadas = 0;      // Cuenta las partidas ganadas

const palabra = document.getElementById("palabraJugador");
const botonComenzar = document.getElementById("comenzarJuego");

// Función para comenzar la partida
function comenzarPartida() {
    const palabraValor = palabra.value;

    document.getElementById("body").style.backgroundColor = "white";

    // Verificar si la palabra es válida
    if (/\d/.test(palabraValor)) {
        alert("La palabra no puede contener números.");
    } else if (palabraValor.length < 4) {
        alert("La palabra no puede contener menos de 4 letras.");
    } else {
        // Reiniciar variables para la nueva partida
        puntos = 0;
        aciertosConsecutivos = 0;

        // Preparar la palabra y deshabilitar el input
        palabraIntroducida();
        palabra.disabled = true;
        botonComenzar.disabled = true;
    }
}

// Cambia el tipo del input de Password a Text y viceversa.
function cambiaTipo() {
    if (palabra.type == "password") {
        palabra.type = "text";
    } else {
        palabra.type = "password";
    }
}

// Preparar la palabra para ser adivinada
function palabraIntroducida() {
    let palabraAdivinar = document.getElementById("palabraSecreta");
    let palabrita = palabra.value;

    // Crear guiones bajos según la longitud de la palabra
    let guiones = "_".repeat(palabrita.length);

    // Mostrar en el elemento h1 ("Comenzar partida")
    palabraAdivinar.textContent = guiones;

    // Separar las letras entre un espacio de 10px
    palabraAdivinar.style.letterSpacing = "10px";
}

// Función con parámetro para obtener el botón pulsado
function solucionPalabra(boton) {
    const letraBoton = boton.textContent.toUpperCase(); // Obtener la letra del botón
    boton.disabled = true; // Deshabilitar el botón pulsado
    const palabraSecreta = palabra.value.toUpperCase(); // Convertir la palabra secreta en mayúsculas
    const palabraAdivinar = document.getElementById("palabraSecreta"); // Elemento que muestra los guiones y letras encontradas
    let estadoActual = palabraAdivinar.textContent.split(""); // Convertir texto a array

    let encontrada = false;
    let ocurrencias = 0;

    // Buscar la letra en la palabra secreta
    for (let i = 0; i < palabraSecreta.length; i++) {
        if (palabraSecreta[i] === letraBoton) {
            estadoActual[i] = letraBoton; // Reemplazar guion en la posición correcta
            encontrada = true;
            ocurrencias++;
        }
    }

    // Actualizar el contenido del elemento con las letras descubiertas
    palabraAdivinar.textContent = estadoActual.join("");

    // Actualizar puntos
    if (encontrada) {
        aciertosConsecutivos++; // Incrementar los aciertos consecutivos
        puntos += aciertosConsecutivos * ocurrencias; // Puntos por ocurrencias
    } else {
        aciertosConsecutivos = 0; // Reiniciar aciertos consecutivos
        puntos = Math.max(0, puntos - 1); // Restar un punto, sin permitir negativos
    }

    // Actualizar la visualización de los puntos en HTML
    document.getElementById("puntos").textContent = puntos;

    // Verificar si la palabra fue completamente descubierta
    if (!estadoActual.includes("_")) {
        totalPartidas++;
        partidasGanadas++;
        finalizarPartida();
    }
}

// Función para finalizar la partida
function finalizarPartida() {
    palabra.disabled = false;
    botonComenzar.disabled = false;

    // Calcular el porcentaje de victorias
    const porcentajeGanadas = ((partidasGanadas / totalPartidas) * 100).toFixed(2);

    // Actualizar la visualización de estadísticas en HTML
    document.getElementById("body").style.backgroundColor = "green";
    document.getElementById("totalPartidas").textContent = totalPartidas;
    document.getElementById("partidasGanadas").textContent = partidasGanadas;
    document.getElementById("porcentajeVictorias").textContent = porcentajeGanadas + "%";

    // Mensaje de fin de partida
    alert(`¡Felicidades! Has adivinado la palabra. Puntos: ${puntos}`);

}
