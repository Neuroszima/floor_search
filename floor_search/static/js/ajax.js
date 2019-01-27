var form = $('.crawlerform');
var crawler_response;
var crawler_status_box = $('.crawler_content');
var stop_status;

form.submit(function (e) {

    e.preventDefault();
    var form_url = $(document).find("#url").val();

    $.ajax({
        type: "json_text",
        url: "http://127.0.0.1:8000/api/crawl/",
        method: "POST",
        data: {
            "url": form_url
        },
        success: function (result) {
            // console.log('Submission was successful.');
            // console.log(data);
            console.log(result);
            crawler_response = result;
            console.log(crawler_response.task_id);
            let show_status = setInterval(crawler_status, 1000);
            stop_status = function () {
                clearInterval(show_status)
            }
        },
        error: function (xhr,status,err) {
            console.log(xhr);
            console.log(status);
            console.log(err);
        },
    });

    function crawler_status() {
        var result;
        $.ajax("http://127.0.0.1:8000/api/crawl/", {
            type: "GET",
            dataType: "json_text",
            data: {
                "task_id": crawler_response.task_id,
                "unique_id": crawler_response.unique_id
            }
            }).done(function (_result) {
                // console.log(result);
                result = _result;

            }).fail(function (xhr,status,err) {
                console.log(xhr);
                console.log(status);
                console.log(err)
            }).always(function(xhr,status) {
                // console.log(form_url, status)
            if (result.status === 'finished'){
                stop_status()
            }
        });
    }
});

