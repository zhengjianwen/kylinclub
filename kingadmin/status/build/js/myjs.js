/**
 * Created by zhengjianwen on 2017/7/18.
 */
$('.showme').click(function () {
            var cid = $(this).attr('data');
            var status = $(this).attr('status');
            $.ajax({
                url:'/kingadmin/news/status/'+ data,
                type:'GET',
                dataType:'JSON',
                data:{'status':status},
                success:function(arg){
                    if (status == 1){
                        $(this).val('显示')
                    }else {
                        $(this).val('隐藏')
                    }

                },
                        })
                    });

$('.myedit').click(function () {
    var name = $(this).parent().prev().text();
    $(this).parent().prev().attr('old',name);
    $(this).parent().prev().html('<input type="text" class="form-control" value="' + name + '">');
    $(this).addClass('hide').next().removeClass('hide')
});

$('.mysave').click(function () {
    var name = $(this).parent().prev().find('input').val();
    var old = $(this).parent().prev('old');
    var that = $(this);
    if (name != old){
        var cid = $(this).parent().prev().prev().text();
        $.ajax({
            url:'/kingadmin/role/edit/' + cid,
            data:{'name':name},
            type:'POST',
            dataType:'JSON',
            success:function (arg) {
                if (arg.status){

                    that.parent().prev().text(name);
                    that.addClass('hide').prev().removeClass('hide');
                }else {
                    alert('更新失败');
                }
            }
        })
    }

});

$('.myuser').click(function () {
    var name = $(this).parent().prev().text();
    var cid = $(this).parent().prev().prev().text();
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $('#role_id').attr('cid',cid).val(name);
    $.ajax({
        url:'/kingadmin/userlist/' + cid,
        type:'GET',
        dataType:'JSON',
        success:function (arg) {
            if(arg.status){
                var roleuser = arg.roleuser;
                var user = arg.user;
                $('#newuser').html('');
                for (var i=0;i<roleuser.length;i++){
                    var option = '<option value="'+ roleuser[i][0] +'">'+ roleuser[i][1]+'</option>';
                    $('#newuser').append(option);
                }
                $('#olduesr').html('');
                for (var i=0;i<user.length;i++){
                    var option = '<option value="'+ user[i][0] +'">'+ user[i][1]+'</option>';
                    $('#olduesr').append(option);
                }


            }
        }
    });

});

$('#adduser').click(function () {
    var tmp = $('#olduesr').html();
    $('#olduesr').html('');
    $('#newuser').append(tmp)
});

$('#deluser').click(function () {
    var tmp = $('#newuser').html();
    $('#newuser').html('');
    $('#olduesr').append(tmp)
});

$('#myrolesave').click(function () {
    var data = [];
     $('#newuser').find('option').each(function () {
           data.push($(this).val())
     });
    var cid = $('#role_id').attr('cid');
    //var data= $('select[name="userdata"]').val();
    //var data1= $('#newuser').val();
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url:'kingadmin/userlist/' + cid,
        type:'POST',
        traditional: true,
        dataType:'JSON',
        data:{'user':data,'csrfmiddlewaretoken':csrf},
        success:function (arg) {
            if(arg.status){
                alert('提交成功');
                $('#myModal').modal('hide')
                }else {
                alert('提交失败')
            }
        }
    });
});

function moveItem(from,to) {
     var toObj = document.getElementById(to);
     var fromObj = document.getElementById(from);
     var len = fromObj.options.length;
     for (var i=0;i<len;i++)
     {
      var option = fromObj.options[i];
      if (option.selected == true)
      {
       toObj.options.add(new Option(option.text,option.value));
       fromObj.options.remove(i);
      }
     }
}