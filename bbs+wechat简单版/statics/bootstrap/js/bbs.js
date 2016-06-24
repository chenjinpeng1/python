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
           '<button style="margin-top: 20px" class="btn btn-primary js-po"onclick="submit_comment(this)" >评论</button>'+
            '</div>')
        }
    })
}
function submit_comment(ths){
        datas = {}
        datas['comment'] = $(ths).siblings().val()
        datas['article_id'] = $.trim($(".article-title-bg").text())
        datas['parent_comment_id'] = $(ths).parent().siblings('.user_info').children("span[name='author_user']").attr("id")
        datas['user_id'] = $(".user").children().first().text()
        datas['comment_type'] = 1
        datas['date']=$(ths).parent().siblings().first().children().last().text()
        base_url = window.location.pathname
        console.log(datas)
        datas_json = JSON.stringify(datas)
    $.ajax({
        type:"POST",
        url:base_url,
        data:{"data":datas_json,
            "csrfmiddlewaretoken":getCsrf()
            },
        success:function(arg) {
            arg = eval(arg)
            console.log(typeof(arg))
            if (arg[0] == "True") {
                console.log("提交成功")
                console.log( datas['parent_comment_id'])
                if ( typeof(datas['parent_comment_id']) == 'undefined') {
                    comment_html = '<hr>+'
                    margin_left = "0px"
                }
                else {
                    margin = parseInt($(ths).parent().parent().attr("style").split(":")[1].split("p")[0])
                    margin += 30
                    margin_left = String(margin) + "px"
                    console.log(margin_left)
                }
                user_img = $(".navbar-right").children("img").attr("src")
                comment_html = '<hr>' +
                    '<div class="A-comment">' +
                    '<div class="pl-box-wrap" style="margin-left:' + margin_left + '">' +
                    '<div class="user_info">' +
                    '<span style="margin-right:20px"><img class="small_img" src="' + user_img + '"></span>' +
                    '<span name="author_user" style="margin-right: 20px">' + datas['user_id'] + '</span>' +
                    '<span style="margin-right: 20px">' + arg[1] +'</span>'  +
                    '<div class="pl-content" style="margin-top: 20px;">' +
                    '<span>' + datas['comment'] + '</span>' +
                    '<span style="padding-right:20px" class="glyphicon glyphicon-thumbs-up pull-right goodlike"> 0</span>' +
                    '<span style="padding-right:20px" class="glyphicon glyphicon-comment pull-right"> 0</span></div> ' +
                    '<div class="glyphicon glyphicon-pencil add_comment" style="color:#666" onclick="add_comment()">我要点评 </div>'
                if (margin_left == "0px"){
                    $(".comment").append(comment_html)
                    $(ths).siblings(".form-control").val("")
                }
                else {
                    $(ths).parent().parent().parent().append(comment_html)
                    $(".comment-text").remove()
                }
            }
        }
    })

}
$(function(){
    $('.pl-content').delegate('.goodlike', 'click', function(ths){
        datas={}
        //parent_comment_id = $(this).parent().siblings(".user_info").children("span[name='author_user']").attr("id")
        datas['article_id'] = $.trim($(".article-title-bg").text())
       base_url =  window.location.pathname
        datas['parent_comment_id'] = $(this).parent().siblings(".user_info").children("span[name='author_user']").attr('id')
        datas['comment_type'] = 2
        datas['user_id'] =  $(".user").children().first().text()
        datas_json = JSON.stringify(datas)
        goodlike = $(this)
        $.ajax({
            type:"POST",
            url:base_url,
            data:{"data":datas_json,
            "csrfmiddlewaretoken":getCsrf()
            },
            success:function(arg){
                if(arg == "True"){
                    console.log("YES!")
                    console.log(goodlike)
                    goodlike.text("100")

                }
                else{
                    console.log("NO!")
                }
            }
        })
    })
})

$(function(){
    add_comment();
    //submit_comment();
    //goodlike()
})