$(document).ready(function () {
    $(".comment-toggle").click(function () {
        $(this).closest(".card-body").find("#comment-toggle-1").toggle(100);

    });
    $(".comment-toggle-2").click(function () {
        $(this).closest(".card").find("#comment-toggle-3").toggle(300);
    });
});
$(function () {
    $(".commentfield").keypress(function (e) {

        if ((e.which == 13) && (!e.shiftKey)) {
            //submit form via ajax, this is not JS but server side scripting so not showing here
            var that = this;
            var body = $(this).val();
            $.ajax({
                url: "{%url 'Posts:postcomment' %}",
                type: 'GET',
                data: { commentbody: $(this).val(), postpk: $(this).closest(".posthead").find("#postid").text() },
                success: function (res) {

                    $(that).closest(".posthead").find("#comment-toggle-3").prepend(`
            <div class="my-2 mx-4 border rounded" style="background-color:#f8f9fa">
            <div class="col mt-3">
                <img src="${res.avatar}" class="rounded-circle mr-1" height="32" alt="Cinque Terre">
                <!--      USER   NAME OF COMMENT AUTHOR -->
                <span>${res.author}</span>
                <span class="float-right text-muted">${res.created}</span>
            </div>
            <!-- write COMMENTS HERE -->
            <div class="col-sm">
                <p class="p-2">
                    ${body}
                </p>
            </div>
        </div>
            
            `);


                }
            });


            $(this).val("");
            e.preventDefault();
            $(this).closest(".card").find("#comment-toggle-3").css("display", "block");

        }
    });
});
