    function Func(){
        $(this).parent().siblings().find('.ChildMenu').addClass('hide')
        $(this).parent().siblings().find(".MasterMenu").removeAttr("style")
        if(!$(this).next().hasClass('hide')){
            $(this).next().addClass('hide');
            $(this).removeAttr("style")
        }else{
            $(this).next().removeClass('hide');
            $(this).attr({style:"background-color:#7B72E9"})
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
    //function highlightRows() {
    //$("tr").hover(
    //    function() {
    //        $(this).css("fontWeight", "bold");
    //    },
    //    function() {
    //        $(this).css("fontWeight", "normal");
    //    }
    //);
//}
    function EditSelect() {
        $("#EditSelect").click(function(){
            var Tmp = $("input:checked").parent().siblings(".Edit");
            if(Tmp.length >= 2) {
                //禁用其他功能
                $("#EditSelect").prop("disabled",true)
                $("#Reverse").prop("disabled", 'true')
                $("input[type='checkbox']").prop("disabled", true)
                $(".EditStyle").prop("disabled", true)
                //获取选中的元素 找到要编辑的元素
                Tmp.each(function () {
                    //获取原数据
                    var TmpDate = ($(this).children('span').text());
                    var IdName = $(this).children('span').attr('IdName')
                    $(this).children('span').addClass('hide')
                    var WriteData = "<input class='Input' type='text' IdName='" + IdName + "' value='" + TmpDate + "'/>";
                    $(this).append(WriteData);
                })
            }
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
                    $("#Reverse").prop("disabled",false)
            })
        })
    }
    function Save(){
        $("#Save").click(function(){
            //匹配被选中的tr
            var CheckedTrue = $("input:checked").parent().parent()
            console.log(CheckedTrue)
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
                //逐行写入数据
                HostInfos=[]
                HostInfo={}
                CheckedTrue.each(function(){
                    HostInfo = {
                        'hostname':$(this).children(".Edit").children("input[idname='HostName']").val(),
                        'id':$(this).children(".Edit").children("input[idname='Id']").val(),
                        'ipaddress':$(this).children(".Edit").children("input[idname='IpAddress']").val(),
                        'port':$(this).children(".Edit").children("input[idname='Port']").val()
                    }
                    HostInfos.push(HostInfo)
                    $(this).children(".Edit").children("span[IdName='HostName']").text(HostInfo['hostname'])
                    $(this).children(".Edit").children("span[IdName='IpAddress']").text(HostInfo['ipaddress'])
                    $(this).children(".Edit").children("span[IdName='Port']").text(HostInfo['port'])
                    })
                    var jsondata = JSON.stringify(HostInfos)
                    $.ajax({
                        type:"POST",
                        url:'/cmdb/HostManage/',
                        //typeType:json,
                        data:{'data':jsondata},
                        success:function(arg) {
                            if(arg == "OK"){
                            alert("保存成功")
                        }},
                        error:function(arg){
                            alert("提交失败")
                        }
                    })
                    $(CheckedTrue).children(".Edit").children("input").remove()
                    $(CheckedTrue).children(".Edit").children("span").removeClass("hide")
                    $(CheckedTrue).children().children("input[type='checkbox']").prop("checked",false)
                    $("input[type='checkbox']").prop("disabled",false)
                    $(".EditStyle").prop("disabled",false)
                    $("#Reverse").prop("disabled",false)
                    $("#EditSelect").prop("disabled",false)

                //return true
            }
        })
    }
    function Add(){
        $("#Add").click(function(){
            $(".EditWindow2").removeClass("hide")
        })
    }
    function AddExit(){
        $(".EditWindowCancel2").click(function(){
            $(".EditWindow2").addClass("hide")
            $(".InfoNameWidth2").children("input").each(function(){
                $(this).val("")
            })
        })
    }
    function AddSub(){
        AddHostInfo={}
        $(".AddSubmit").click(function(){
            console.log($(".InfoNameWidth2").children("#Addhostname"))
            AddHostInfo['hostname']=$(".InfoNameWidth2").children("#Addhostname").next().val()
            AddHostInfo['ipaddress']=$(".InfoNameWidth2").children("#Addhost_address").next().val()
            AddHostInfo['port']=$(".InfoNameWidth2").children("#Addhost_port").next().val()
            console.log(AddHostInfo)
            $(".EditWindow2").addClass("hide")
            data = JSON.stringify(AddHostInfo)
            //$.ajax({
            //    type:"POST",
            //    url:"/cmdb/AddHost/",
            //    data:{"data":data},
            //    success:function(arg){
            //        //if (arg == "OK"){
            //        //    alert(aa)}
            //        //else{
            //        //    alert(arg)
            //        //}
            //        alert("OK")
            //
            //    },
            //    error:function(arg){
            //        alert("提交失败")
            //    }
            //})
        })
    }
    function EditStyle(){
        //$(".EditStyle").click(function(){
            $(this).parent().siblings().children(".OptionStyle").prop("checked",true)
            //获取编辑的信息
            var SourceHostname = $("input:checked").parent().siblings(".Edit").children("span[IdName='HostName']").text()
            var SourceHostaddress = $("input:checked").parent().siblings(".Edit").children("span[IdName='IpAddress']").text()
            var SourceHostport = $("input:checked").parent().siblings(".Edit").children("span[IdName='Port']").text()
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
        $(".Sub").click(function(){
            var MatchTrue = true
            $(".edit_css").addClass("hide")
            var Tmp = $(".EditWindow").children();
            var ID = $("input:checked").parent().next().children("span").text()
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
                data = {
                    'id':ID,
                    'hostname':Hostname,
                    'ipaddress':Hostaddress,
                    'port':Hostport,
                }
                jsondata = JSON.stringify(data)
                $.ajax({
                    type:'POST',
                    url:'/cmdb/selectedit/',
                    data:{'data':jsondata},
                    success:function(arg){
                            alert("提交成功")
                    },
                    error:function(arg){
                        alert("提交失败")
                    }
                })
                $("input:checked").parent().siblings(".Edit").children("span[IdName='HostName']").text(Hostname)
                $("input:checked").parent().siblings(".Edit").children("span[IdName='IpAddress']").text(Hostaddress)
                $("input:checked").parent().siblings(".Edit").children("span[IdName='Port']").text(Hostport)
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
    //highlightRows();
    Cancel();
    Save();
    Add();
    AddExit();
    AddSub();
    //EditStyle();
    EditWindowSubmit();
    EditWindowCancel();
})