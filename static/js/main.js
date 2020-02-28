function _readSensorValue() {

    $.ajax({
        url: '/read-sensor-value',
        type: 'GET',
        data: 'sendData',

        success: function (response) {
            let receiveData = $.parseJSON(response).data;
            console.log(receiveData);
            $('#sensor_value1').html(receiveData.sensor1);
            $('#sensor_value2').html(receiveData.sensor2);
            $('#sensor_value3').html(receiveData.sensor3);
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
                $('#sensor_value4').html(receiveData.sensor4);
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



