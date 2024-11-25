$(document).ready(function () {
    $.getJSON('/data/Promedio_calificacion_Productos', function (data) {
        Highcharts.chart('Promedio_calificacion_Productos', {
            chart: { type: 'bar' },
            title: { text: ' ' },
            xAxis: { type: 'category', title: { text: 'Productos' } },
            yAxis: { title: { text: 'Promedio (1 a 5)' }, max: 5, min: 0 },
            series: [{ name: 'Promedio', data: data }]
        });
    });

    $.getJSON('/data/Cantidad_categorias_Productos', function (data) {
        Highcharts.chart('Cantidad_categorias_Productos', {
            chart: { type: 'pie' },
            title: { text: ' ' },
            series: [{ name: 'Categorías', data: data }]
        });
    });

    $.getJSON('/data/Cantidad_stock_Productos', function (data) {
        Highcharts.chart('Cantidad_stock_Productos', {
            chart: { type: 'column' },
            title: { text: ' ' },
            xAxis: { type: 'category', title: { text: 'Productos' } },
            yAxis: { title: { text: 'Cantidad' } },
            series: [{ name: 'Stock', data: data }]
        });
    });

    $.getJSON('/data/pedidos_por_mes', function (data) {
        Highcharts.chart('pedidos_por_mes', {
            chart: { type: 'line' },
            title: { text: ' ' },
            xAxis: { type: 'category', title: { text: 'Mes' } },
            yAxis: { title: { text: 'Cantidad' } },
            series: [{ name: 'Pedidos', data: data }]
        });
    });

    $.getJSON('/data/usuarios_por_mes', function (data) {
        Highcharts.chart('usuarios_por_mes', {
            chart: { type: 'line' },
            title: { text: ' ' },
            xAxis: { type: 'category', title: { text: 'Mes' } },
            yAxis: { title: { text: 'Cantidad' } },
            series: [{ name: 'Usuarios', data: data }]
        });
    });

    $.getJSON('/data/productos_entregados', function (data) {
        $('#productos_entregados').text(data[0].total);
    });
    $.getJSON('/data/productos_cancelados', function (data) {
        $('#productos_cancelados').text(data[0].total);
    });
    $.getJSON('/data/productos_EnProceso', function (data) {
        $('#productos_EnProceso').text(data[0].total);
    });
    $.getJSON('/data/ganancias_por_mes', function (data) {
        Highcharts.chart('ganancias_por_mes', {
            chart: { type: 'column' },
            title: { text: ' ' },
            xAxis: { type: 'category', title: { text: 'mes' } },
            yAxis: { title: { text: 'ganancias' } },
            series: [{ name: 'ganancias', data: data }]
        });
    });
});