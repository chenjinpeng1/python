    function Func(){
        $(this).parent().siblings().find('.ChildMenu').addClass('hide')
        $(this).parent().siblings().find(".MasterMenu").removeAttr("style")
        if(!$(this).next().hasClass('hide')){
            $(this).next().addClass('hide');
            $(this).removeAttr("style")
        }else{
            $(this).next().removeClass('hide');
            $(this).attr({style:"background-color:#005383"})
        }
    }
    function HostMenu(){
        $("#HostMenu").click(function(){
            if($(".RightBody").hasClass("hide")) {
                $(".RightBody").removeClass("hide")
            }else{
                $(".RightBody").addClass("hide")
            }
        })
    }
    function SelectAll(){
        $("#SelectAll").click(function(){
            $("input[type='checkbox']").prop("checked", true)
        })
    }
    function Reverse(){
        $("#Reverse").click(function(){
             $("input[type='checkbox']").each(function(){
                var Tmp = $(this).prop("checked")
                 if(Tmp){
                     $(this).prop("checked",false)
                 }else{
                     $(this).prop("checked",true)
                 }}
            )
        })
    }
    function highlightRows() {
    $("tr").hover(
        function() {
            $(this).css("fontWeight", "bold");
        },
        function() {
            $(this).css("fontWeight", "normal");
        }
    );
}
    function EditSelect() {
        $("#EditSelect").click(function(){
            //禁用其他功能
            $("#Reverse").prop("disabled",'true')
            $("input[type='checkbox']").prop("disabled",true)
            $(".EditStyle").prop("disabled",true)
            //获取选中的元素 找到要编辑的元素
            var Tmp = $("input:checked").parent().siblings(".Edit");
            Tmp.each(function(){
                //获取原数据
                var TmpDate=($(this).children('span').text());
                var IdName = $(this).children('span').attr('IdName')
                $(this).children('span').addClass('hide')
                var WriteData="<input class='Input' type='text' IdName='"+ IdName +"' value='" + TmpDate +"'/>";
                $(this).append(WriteData);
            })
        })
    }
    function Cancel(){
        $("#Cancel").click(function(){
            $("input[type='checkbox']").prop("disabled",false)
            $(".EditStyle").prop("disabled",false)
            var Tmp = $("input:checked").parent().siblings(".Edit");
            console.log(Tmp)
                Tmp.each(function(){
                //获取原数据
                var TmpDate=($(this).children().val());
                //<td class="Edit">nginx</td>
                //var WriteData="<td class='Edit'>" + TmpDate + "</td>" ;
                //$(this).html(TmpDate);
                    $(this).children('span').removeClass('hide')
                    $(this).children('input').remove()
                    $("input[type='checkbox']").prop("checked",false)
            })
        })
    }
    function Save(){
        $("#Save").click(function(){
            //匹配被选中的tr
            var CheckedTrue = $("input:checked").parent().parent()
            //console.log(CheckedTrue)
            var MatchTrue = true
            //循环用户写入的数据，判断是否正确
            CheckedTrue.each(function(){
                //匹配tr下可编辑模式的元素
                var AllInput = $(this).children(".Edit").children("input");
                AllInput.each(function(){

                    if($(this).attr("IdName") == 'hostname'){
                        if($(this).val().length > 10){
                            alert("主机名长度不能大于10");
                            MatchTrue = false;
                            return false;
                        }
                    }
                    if($(this).attr("IdName") == 'ipaddress'){
                        if($(this).val().match(/^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/)==null){
                            alert("IP地址格式错误");
                            MatchTrue = false
                            return false;
                        }
                    }
                    if($(this).attr("IdName") == 'port'){
                        NumChange=Number($(this).val())
                        if(NumChange){
                            if($(this).val() > 65535 || $(this).val() <=0){
                                alert("端口范围在1~65535");
                                MatchTrue = false
                                return false;
                            }
                        }else{
                            alert("不是数字")
                            MatchTrue = false
                            return false;
                            }
                        }
                })
                if(!MatchTrue){
                    return false
                }
            })
            if(MatchTrue){
                alert("验证通过")
                //逐行写入数据
                HostInfo={}
                CheckedTrue.each(function(){
                    HostInfo['hostname']=$(this).children(".Edit").children("input[idname='hostname']").val();
                    HostInfo['ipaddress']=$(this).children(".Edit").children("input[idname='ipaddress']").val();
                    HostInfo['port']=$(this).children(".Edit").children("input[idname='port']").val();
                    $(this).children(".Edit").children("span[IdName='hostname']").text(HostInfo['hostname'])
                    $(this).children(".Edit").children("span[IdName='ipaddress']").text(HostInfo['ipaddress'])
                    $(this).children(".Edit").children("span[IdName='port']").text(HostInfo['port'])
                    $(this).children(".Edit").children("input").remove()
                    $(this).children(".Edit").children("span").removeClass("hide")
                    $(this).children().children("input[type='checkbox']").prop("checked",false)
                    $("input[type='checkbox']").prop("disabled",false)
                    $(".EditStyle").prop("disabled",false)
                })
            }
        })
    }
    function Add(){
        $("#Add").click(function(){
            $("table").append('<tr> ' +
                    '<td><input class="OptionStyle" type="checkbox"/></td>' +
                    '<td class="Edit"><span IdName="hostname"></span></td>'+
                    '<td class="Edit"><span IdName="ipaddress"></span></td>'+
                    '<td class="Edit"><span IdName="port"></span></td>'+
                    '<td><input class="EditStyle" type="button" value="编辑"/></td>'+
                    '</tr>')
        })
    }
    function EditStyle(){
        //$(".EditStyle").click(function(){
            $(this).parent().siblings().children(".OptionStyle").prop("checked",true)
            //获取编辑的信息
            var SourceHostname = $("input:checked").parent().siblings(".Edit").children("span[IdName='hostname']").text()
            var SourceHostaddress = $("input:checked").parent().siblings(".Edit").children("span[IdName='ipaddress']").text()
            var SourceHostport = $("input:checked").parent().siblings(".Edit").children("span[IdName='port']").text()
            console.log(SourceHostname)
            $(".EditWindow").children().children("span[id='hostname']").next().val(SourceHostname)
            $(".EditWindow").children().children("span[id='host_address']").next().val(SourceHostaddress)
            $(".EditWindow").children().children("span[id='host_port']").next().val(SourceHostport)
            $(".EditWindow").removeClass("hide");
            $(".OptionStyle").prop("disabled",true)
            $(".RightDis").children("input[type='button']").prop("disabled",true)
            $(".EditStyle").prop("disabled",true)
        //})

    }
    function EditWindowSubmit(){
        $(".EditWindowSubmit").click(function(){
            var MatchTrue = true
            console.log("aaaa1")
            $(".edit_css").addClass("hide")
            var Tmp = $(".EditWindow").children();
            var Hostname = $(".EditWindow").children().children("#hostname").next().val()
            var Hostaddress = $(".EditWindow").children().children("#host_address").next().val()
            var Hostport = $(".EditWindow").children().children("#host_port").next().val()
            Tmp.each(function(){
                console.log(MatchTrue)
                if($(this).children("span").attr("id") == "hostname") {
                    var hostname = $(this).children("input").val()
                    if (hostname.length > 10 || hostname.length == 0) {
                        $(this).children("label").removeClass("hide")
                        MatchTrue = false
                        return false
                    }
                }
                if($(this).children("span").attr("id") == "host_address") {
                    var hostaddress = $(this).children("input").val()
                    if (hostaddress.match(/^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/)==null) {
                        $(this).children("label").removeClass("hide")
                        MatchTrue=false
                        return false
                    }
                }
                if($(this).children("span").attr("id") == "host_port"){
                    var hostport = $(this).children("input").val()
                    NumChange=Number(hostport)
                    if(NumChange){
                        if(hostport > 65535 || hostport <=0){
                        $(this).children("label").next().removeClass("hide")
                            MatchTrue = false
                            return false;
                        }
                    }else{
                        $(this).children("label").next().siblings().removeClass("hide")
                        MatchTrue = false
                        return false;
                        }
                }

            })
            if(MatchTrue){
                $(".EditWindow").addClass("hide");
                console.log($("input:checked"))
                $("input:checked").parent().siblings(".Edit").children("span[IdName='hostname']").text(Hostname)
                $("input:checked").parent().siblings(".Edit").children("span[IdName='ipaddress']").text(Hostaddress)
                $("input:checked").parent().siblings(".Edit").children("span[IdName='port']").text(Hostport)
                $("input:checked").prop("checked",false)
                $(".OptionStyle").prop("disabled",false)
                $(".RightDis").children("input[type='button']").prop("disabled",false)
                $(".EditStyle").prop("disabled",false)

            }
    })
    }
    function EditWindowCancel(){
        $(".EditWindowCancel").click(function(){
            $(".EditWindow").addClass("hide")
            $("input:checked").prop("checked",false)
            $(".OptionStyle").prop("disabled",false)
            $(".RightDis").children("input[type='button']").prop("disabled",false)
            $(".EditStyle").prop("disabled",false)
        })
    }
$(function(){
    $('body').delegate('.MasterMenu','click',Func);
    $("table").delegate('.EditStyle','click',EditStyle);
});
$(function(){
});

$(function(){
    HostMenu();
    SelectAll();
    Reverse();
    EditSelect();
    highlightRows();
    Cancel();
    Save();
    Add();
    //EditStyle();
    EditWindowSubmit();
    EditWindowCancel();
})