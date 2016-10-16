/**
 * Created by Administrator on 2016/9/8.
 */

function getCsrf(){
    return $("input[name='csrfmiddlewaretoken']").val();
}

function asset_update(){
    $("a[name='update']").click(function(){
        var hostid = $(this).attr("value")
        //$.post("{% url 'asset_report' %}",
        //    {
        //        'hostid':JSON.stringify(hostid)
        //    },
        //    function(callback){
        //        console.log(callback)
        //    }
        //)
        $.ajax({
            type:"POST",
            url:"/manage/asset_report/",
            data:{"hostid":JSON.stringify(hostid),
            'csrfmiddlewaretoken':getCsrf()
            },
            success:function(callback){
                console.log(callback)
            }
        })
    })
}
$(function(){
    asset_update();
})