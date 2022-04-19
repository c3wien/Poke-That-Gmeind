// show mobile share links

if (!navigator.userAgent.match(/iPhone|iPad|Android/i)) {
    $('.share-mobile').css("cssText", "display: none !important;");
}

// smooth scroll
$(document).ready(function () {
    $("a[href*='#']:not([href='#'])").click(function() {
        if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'')  || location.hostname == this.hostname) {
            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
            if (target.length) {
                $('html,body').animate({
                    scrollTop: target.offset().top
                }, 800);
                return false;
            }
        }
    });
});

// be-active section
$(document).ready(function() {
    var $beActive = $('#be-active');
    var containers = $beActive.find('.container');
    
    if ($beActive && containers.length > 2) {
        var $container1 = $(containers[0]);
        var $container2 = $(containers[1]);
        var $container3 = $(containers[2]);
        
        $('#be-active-button').on('click', function () {
            $container1.hide();
            $container2.show();
        });
        
        $('#be-active-form').on('submit', function(e) {
            e.preventDefault();
            var postUrl = $(this).attr("action"); //get form action url
            var formData = $(this).serialize(); //Encode form elements for submission

            $.post( postUrl, formData) 
                .done(function(data) {
                    console.log(data.status);
                    if (data.status == 'success') {
                        $container2.hide();
                        $container3.show();
                    } else {
                        if (data.reason == 'already_subscribed') {
                            $("#be-active-server-error").html('Du bist bereits eingetragen.');
                        } else {
                            $("#be-active-server-error").html('Ein Fehler ist aufgetreten. Bitte versuche es später nochmal!');
                        }
                    }
                })
                .fail(function(xhr, status, error) {
                    $("#be-active-server-error").html('Ein Fehler ist aufgetreten. Bitte versuche es später nochmal!');    
                });
            
                
        });
        
        $('#be-active-back').on('click', function() {
            $container3.hide();
            $container1.show();
        });
    }
});

$(document).ready(function() {
    if ($("#videos-carousel").length > 0) {
        var videocarousel = $("#videos-carousel").slick({
            dots: true,
            infinite: true,
            slidesToShow: 1,
            slidesToScroll: 1,
            adaptiveHeight: true,
            responsive: [
                {
                    breakpoint: 992,
                    settings: {
                        dots: false
                    }
                }
            ]
        });

        videocarousel.on("beforeChange", function(event, slick, currentSlide, nextSlide) {
            var iframe = $("#videos-carousel .slick-current iframe");
            if (iframe.length > 0) {
                var iframeWindow = iframe.get(0).contentWindow;
                iframeWindow.postMessage('{"event":"command","func":"pauseVideo","args":""}', '*');
            }
        });
    }
});


// search filter
var timeout = null
$(document).ready(function() {
    if($("#cities").length) {
        $("#states :checkbox").change(search);
        // $("#name input").on('keyup change', search);
        $("#name input").on('keyup change', function() {
           clearTimeout(timeout);
           timeout= setTimeout(search, 10)
        });
    }
});

function search(event) {
    $("#cities").children(".city").each(function() {
        var name = $(this).data("name").toLowerCase() + $(this).data("plz");
        if(
          ($("#state-" + $(this).data("state")).prop("checked") || $("#states").children(":checked").length == 0)
          && ($("#name input").val() === '' || name.indexOf($("#name input").val().trim().toLowerCase()) > -1)
        ) {
            $(this).removeClass("invisible");
        } else {
            $(this).addClass("invisible");
        }
    });
}

// mail text filter
$(document).ready(function() {
    if($("#mail").length) {
        mailReps = $("#mail .textarea").text();
        updateText();
        $("#mail-firstname").keyup(updateText);
        $("#mail-lastname").keyup(updateText);
    }
})

function updateText(event) {
    var lines = mailReps.split("\n");
    var MailNameFrom = $("#mail-firstname").val() + " " + $("#mail-lastname").val();
    if(!$.trim(MailNameFrom).length) {
        MailNameFrom = "Dein Name";
    }
    $("#mail .textarea").empty();
    $.each(lines, function() {
        if(this.length) {
            str = this.replace("{name_city}", MailNameTo).replace("{name_user}", MailNameFrom);
            $("#mail .textarea").append("<p>" + str + "</p>");
        }
    });
}

/*
 * Convert a string into a date.
 */
function convertStringToDate(stringdate)
{
    // Internet Explorer does not like dashes in dates when converting,
    // so lets use a regular expression to get the year, month, and day
    var DateRegex = /([^-]*)\/([^-]*)\/([^-]*)/;
    var DateRegexResult = stringdate.match(DateRegex);
    var DateResult;
    var StringDateResult = "";

    // try creating a new date in a format that both Firefox and Internet Explorer understand
    try
    {
        DateResult = new Date(DateRegexResult[1]+"/"+DateRegexResult[2]+"/"+DateRegexResult[3]);
    }
        // if there is an error, catch it and try to set the date result using a simple conversion
    catch(err)
    {
        DateResult = new Date(stringdate);
    }

    // Date formating
    StringDateResult = (DateResult.getMonth()+1)+"/"+(DateResult.getDate())+"/"+(DateResult.getFullYear());

    return StringDateResult;
}

/*
 * Convert a date into a string.
 */
function convertDateToString(date)
{
    // Add "0" ahead the month & day if needed
    var month = date.getMonth()+1;
    var day = date.getDate();

    if (month < 10) {
        month = "0"+month;
    }
    if (day < 10) {
        day = "0"+day;
    }
    // Date formating
    StringDateResult = month+"/"+day+"/"+(date.getFullYear());

    return StringDateResult;
}

// register video embeds

$(document).ready(function() {
    $("body").on("click", ".video-embed", function (e) {
        var vid = $(this).data("vid");
        var width = $(this).attr('width');
        var height = $(this).attr('height');
        $(this).replaceWith('<iframe width="' + width + '" height="' + height + '" src="https://www.youtube.com/embed/' + vid + '?autoplay=1&enablejsapi=1" frameborder="0" allowfullscreen="allowfullscreen"></iframe>');
    });
});


$(document).ready(function() {
    $("input[name='filterOrigin']").change(function () {
        tableSettings.filterOrigin = $("input[name='filterOrigin']:checked").val();
        refreshTable();
    });

    $("#filterNameButton").click(function () {
        tableSettings.filterName = $("input[name='filterName']").val().trim();
        refreshTable();
    });

    $("input[name='filterName']").on("keyup", function (e) {
        if (e.keyCode == 13) {
            tableSettings.filterName = $("input[name='filterName']").val().trim();
            refreshTable();
        }
    });

    $("select[name='filterTopic']").change(function () {
        tableSettings.filterTopic = $("select[name='filterTopic']").val();
        refreshTable();
    });

    $("th.sortable").click(function () {
        var sortKey = $(this).data("sortKey");
        setSortKey(sortKey);
    });

    $("body").on("click", ".commentOpener", function () {
        var commentId = $(this).data("comment");
        var comment = $("#comment" + commentId);
        comment.toggle();

        if (comment.css("display") == "none") {
            // comment is now hidden
            $(this).removeClass("fa-chevron-circle-up").addClass("fa-chevron-circle-down");
        } else {
            // comment is now shown
            $(this).removeClass("fa-chevron-circle-down").addClass("fa-chevron-circle-up");
        }
    });
});
