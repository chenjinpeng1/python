/**
 * Created by Administrator on 2016/6/14.
 */
//start csrf
// using default ajax csff
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
console.log(csrftoken)
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
//end csrf
function OpenChatWindow(ths){
    $(ths).addClass("active");
    $(ths).siblings().removeClass("active"); //溢出其他的active
    var contact_id = $(ths).attr("contact-id");
    var contact_type = $(ths).attr("contact-type");
    $(".chat-box-title").attr("contact-type",contact_type)
    $(".chat-box-title").attr("contact-id",contact_id)
    var contact_name = $(ths).children(".name").text();
    var chat_box_title_content = '<div style="text-align: center"><span>正在与 ' + contact_name + ' 聊天</span></div>';
    $(".chat-box-title").html(chat_box_title_content)
}
$(document).ready(function(){

$("body").delegate("textarea","keydown",function(e){
    if(e.which == 13){
        // 回车键绑定事件
        var msg_text = $("textarea").val();
        if($.trim(msg_text).length > 0){
            SendMsg(msg_text);
        }
        AddSentMsgIntoBox(msg_text);
        $("textarea").val("")
    }
})
function AddSentMsgIntoBox(msg_text) {
    var user = $(".collapse").find(".user").text()
    var user_img = $(".navbar").find(".small_img").attr("src")
    var new_msg_ele = '<div style="margin-left: 65%" class="msg-item">' +
        '<span style="margin-right: 10px"><img class="small_img" src="' + user_img +'"></span>' +
        '<span style="margin-right: 10px">' + user + '</span>' +
        '<span>' + new Date().toLocaleString() + '</span>' +  //new Date().toLocaleString()获取当前时间
        '<div class="msg-text">' + msg_text + '</div>' + '</div>'
    $(".chat-box-window").append(new_msg_ele)
    $(".chat-box-window").animate({ //animate 动画效果,对匹配到的元素做什么动画效果
        scrollTop: $(".chat-box-window")[0].scrollHeight
    }, 500)
}
function SendMsg(msg_text){
    var user_id = $(".user").attr("user_id")
    var contact_type = $(".chat-box-title").attr("contact-type")
    var contact_id = $(".chat-box-title").attr("contact-id")
    if(contact_type && contact_id){
        var msg_item = {
        'form': user_id,
        'to': contact_id,
        'type':contact_type,
        'msg':msg_text
     }
        $.post("msg_send/",{data:JSON.stringify(msg_item)},function(callback){
            console.log(callback)
        })
    }
}
})

