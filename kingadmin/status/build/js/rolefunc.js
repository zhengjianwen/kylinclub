/**
 * Created by zhengjianwen on 2017/7/18.
 */
$('input[type="checkbox"]').click(function () {
            $('input[type="submit"]').removeClass('hide');
            $('input[type="reset"]').removeClass('hide');
        });
        $('input[type="reset"]').click(function () {
            $(this).addClass('hide');
            $('input[type="submit"]').addClass('hide');
        });
        $('#call').click(function () {
            $('input[type="checkbox"]').each(function () {
                $(this).prop('checked',true);
                $('input[type="submit"]').removeClass('hide');
                $('input[type="reset"]').removeClass('hide');
            })
        });
        $('#fanxuan').click(function () {
            $('input[type="checkbox"]').each(function () {
                var status = $(this).prop('checked');
                if (status){
                    $(this).prop('checked',false);
                }else {
                    $(this).prop('checked',true);
                }
            });
            $('input[type="submit"]').removeClass('hide');
            $('input[type="reset"]').removeClass('hide');
        });
        $('.gongneng').click(function () {
             var gn = $(this).attr('gn');
            $('input[type="checkbox"]').each(function () {
                var status = $(this).attr('func');
                if (status == gn){
                    $(this).prop('checked',true);
                }else {
                    $(this).prop('checked',false);
                }
            });
            $('input[type="submit"]').removeClass('hide');
            $('input[type="reset"]').removeClass('hide');
        });