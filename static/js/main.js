function _readSensorValue() {

    $.ajax({
        url: '/read-sensor-value',
        type: 'GET',
        data: 'sendData',

        success: function (response) {
            let receiveData = $.parseJSON(response).data;
            console.log(receiveData);
            $('#sensor_value1').html(receiveData[0].value);
            $('#sensor_value2').html(receiveData[1].value);
        },
        error: function (error) {
            console.log(error)
        }
    });


}
$(function () {
    $('input').on('click', function () {
        $.ajax({
            url: '/read-sensor-request',
            type: 'GET',
            data: 'sendData',

            success: function (response) {
                let receiveData = $.parseJSON(response).data;
                console.log(receiveData);
                $('#sensor_value3').html(receiveData[2].value);
            },
            error: function (error) {
                console.log(error)
            }
            });
    });
});

//main.initializePageChart();

intervalID = setInterval(_readSensorValue, 1000);

// export {main}



