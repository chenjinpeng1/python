/**
 * Created by Administrator on 2016/6/1.
 */
function deleted_selected(){
    var ID = []
    var select_true = "False"
    $(".select_options").click(function(){
    select = $("select[name='action']").children("option:selected");
    selected_value=select.val()
    if(selected_value != '-------'){

        brothors = $("input:checked").parent().siblings()
        brothors.each(function(){
            if ($(this).attr('name') == "id"){
                tmp = $(this).children("a").text()
                ID.push(tmp)
                select_true = "True"
            }
        })

        if (select_true == "True"){
            base_url=window.location.pathname;
            var jsondata = JSON.stringify({'id':ID})
            $.ajax({
                type:"POST",
                url: base_url,
                data:{'data':jsondata},
                success:function(arg){
                    if (arg == "True"){
                        alert("操作成功")
                        window.location.reload()
                    }
                    else {
                        alert("操作失败")
                    }
                },
                error:function(arg){
                    alert("操作失败")
                }
                })
        }}
        })
}

function all_selected(){
    $(".all_selected").click(function(){
        if ($(".all_selected").prop("checked") == true) {
            $("input[type='checkbox']").prop("checked", true)
        }
        else{
            $("input[type='checkbox']").prop("checked", false)
        }
    })
}

function Auto_search(){
    $(".AutoSearch").keyup(function(){
        search_data = JSON.stringify({'search':$(".AutoSearch").val()})
        base_url=window.location.pathname;
        $.ajax({
            type:'POST',
            url:base_url,
            data: {"data":search_data},
            success:function(arg){
                console.log(arg.length)
                if (arg){
                    $("tbody").remove() //移除tbody 重新排列查询的数据
                    var args = eval(arg) //将后端返回的json数据生成对象
                    $("table").append("<tbody></tbody>")
                    for( line in args){
                        //if ( line == 0){ //line=0表示第一行数据
                        value = "<tr id =" + line +"><td><input type='checkbox'></td></tr>" //格式化添加的内容
                        $("table tbody").append(value)
                        for( list in args[line] ){ //循环第一行数据 取td
                            if(list == 0){
                                value="<td name="+args[line][list][0] + ">" + "<a href=" + args[line][list][1] +">" + args[line][list][1] +" </a></td>"
                                pd = "tbody tr" + "#"+line
                                $(pd).append(value)
                            }
                            else {
                                console.log('---',args[line][list][1])
                                value = "<td name="+args[line][list][0] + ">" + "<label>" +args[line][list][1] +"</label></td>"
                                pd = "tbody tr" + "#"+line
                                $(pd).append(value)
                            }
                        }
                    }
                        //else {
                        //    value = "<tr id =" + line +"><td><input type='checkbox'></td></tr>"
                        //    $("table tbody").append(value)
                        //    for( list in args[line] ){ //循环第n行数据 取td
                        //        if(list == 0){
                        //            value="<td><a href=" + args[line][list][1] + ">" + args[line][list][1] +" </a></td>"
                        //            pd = "tbody tr" + "#"+line
                        //            $(pd).append(value)
                        //        }
                        //        else {
                        //            //value = "<td>" +args[line][list][1] +"</td>"
                        //            value = "<td><label>" +args[line][list][1] +"</label></td>"
                        //            pd = "tbody tr" + "#"+line
                        //            $(pd).append(value)
                        //        }
                        //    }
                        //}
                    //}
                    $("tbody").append("</tr></tboty>")
                }
                else{
                    console.log("null")
                    }
                }
        })
})
}
$(function(){
    deleted_selected();
    all_selected();
    Auto_search();
});