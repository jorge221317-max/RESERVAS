async function cargarTurnos() {
    const res = await fetch("/turnos");
    const turnos = await res.json();
    const tbody = document.querySelector("#tabla-turnos tbody");
    tbody.innerHTML = "";
    turnos.forEach(turno => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${turno.id}</td>
            <td>${turno.fecha}</td>
            <td>${turno.hora}</td>
            <td>${turno.reservado ? "RESERVADO" : "LIBRE"}</td>
            <td>
                <button onclick="reservar(${turno.id})" ${turno.reservado ? "disabled" : ""}>Reservar</button>
            </td>
        `;
        tbody.appendChild(row);
    });
}

async function reservar(id) {
    const formData = new FormData();
    formData.append("turno_id", id);
    const res = await fetch("/turnos/reservar", { method: "POST", body: formData });
    const data = await res.json();
    alert(data.message);
    cargarTurnos();
}

window.onload = cargarTurnos;
