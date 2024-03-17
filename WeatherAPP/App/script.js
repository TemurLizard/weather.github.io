fetch('https://api.openweathermap.org/data/2.5/weather?q=Sheffield&appid=e4b3063181d69feced8cbb4f5de939d4')
    .then(response => response.json())
    .then(response => {
    console.log(response);

    let temp = response.main.temp.toFixed(0)

    document.getElementById("city").innerHTML = response.name;
    document.getElementById("temp").innerHTML = temp - 273 + "°C";
    document.getElementById("pressure").innerHTML = "Pressure " + response.main.pressure ;

})
    .catch(err => {
    console.log(err);
});