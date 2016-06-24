/**
 * Created by Administrator on 2016/6/7.
 */
function add_comment(){
    $(".add_comment").click(function() {
        //console.log("我要点评啊,快点做好")
        if($(this).siblings().hasClass("comment-text")) {
            $(this).parent().find(".comment-text").remove()
        }
        else {
        $(this).parent().append('' +
            '<div class="comment-text" style="margin-top: 20px">' +
            '<textarea class="form-control" placeholder="客观，八字起评,不讲价呦。"></textarea>' +
           '<button style="margin-top: 20px" class="btn btn-primary js-po" onclick="submit_comment(this)">评论</button>'+
            '</div>')
        }
    })
}
function submit_comment(ths){
        data = {}
        data['comment'] = $(ths).siblings().val()
        data['article'] = $.trim($(".article-title-bg").text())
        data['parent_comment'] = $(ths).parent().siblings('.pl-content').children().first().text()
        data['user'] = $(".user").children().first().text()
        base_url = window.location.pathname
        console.log(data)

        datas = JSON.stringify(data)
    $.ajax({
        type:"POST",
        url:base_url,
        data:{"data":datas,
        'csrfmiddlewaretoken':getCsrf()},
        success:function(arg){
            console.log("提交成功")
            if (data["parent_comment"].length == 0){
            console.log('---fuji',data["parent_comment"].length)
                $(".comment").append("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            }
            else{
                margin =parseInt($(ths).parent().parent().attr("style").split(":")[1].split("p")[0])
                margin += 30
                margin_left = String(margin)+"px"
                console.log(margin_left)
                user_img = $(".navbar-right").children("img").attr("src")
                $(ths).parent().parent().parent().append('<hr>' +
                    '<div class="A-comment">' +
                    '<div class="pl-box-wrap" style="margin-left:%s">' +
                    '<div><span style="margin-right:20px"><img src="%s"></span>' +
                    '<span name="author_user" style="margin-right: 20px">%s</span>' +
                    '<span style="margin-right: 20px">%s</span></div>' +
                    '<div class="pl-comment" style="margin-top: 20px;">' +
                    '<span>%s评论内容</span>' +
                    '<span style="padding-right:20px" class="glyphicon glyphicon-thumbs-up pull-right"> %s</span>' +
                    '<span style="padding-right:20px" class="glyphicon glyphicon-comment pull-right"> %s</span></div> ' +
                    '<div class="glyphicon glyphicon-pencil add_comment" style="color:#666">我要点评 </div>'%(margin_left,user_img,)
                    )
            }
        }
    })

}
$(function(){
    add_comment();
    //submit_comment();
})