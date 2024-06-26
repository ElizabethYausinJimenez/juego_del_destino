<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    <title>Futuro</title>
</head>
<body>
    <div class="container">
        <h5>Soy el adivino del Dojo, <span class="text-success">{{session["usuario"]}}</span>  tendrá un viaje muy largo dentro de <span class="text-primary">{{session["numero"]}}</span>
            años a <span class="text-warning">{{session["lugar"]}}</span> y estará el resto de sus días preparando <span class="text-info">{{session["comida"]}}</span> para
            todas las personas que quiere.</h5>
    </div>
    <a href="/volver" class="btn btn-primary ms-5">Jugar de nuevo</a>
</body>
</html>
