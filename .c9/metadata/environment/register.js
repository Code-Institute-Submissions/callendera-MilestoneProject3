{"changed":true,"filter":false,"title":"register.js","tooltip":"/register.js","value":"","undoManager":{"mark":26,"position":30,"stack":[[{"start":{"row":0,"column":0},"end":{"row":41,"column":3},"action":"insert","lines":["$(function(){","    $(\"#register\").on('click', function(event){","        event.preventDefault();","        var fullname   = $(\"#fullname\").val();","        var email      = $(\"#email\").val();","        var password   = $(\"#password\").val();","        var cpassword  = $(\"#cpassword\").val();","        var dob        = $(\"#dob\").val();","        var country    = $(\"#country\").val();","        var gender     = $('input[name=\"gender\"]:checked').val(); ","        var calorie    = $('input[name=\"calorie\"]:checked').val(); ","        var salt       = $('input[name=\"salt\"]:checked').val();","        var terms      = $('input[name=\"terms\"]:checked').val();","        if(!fullname || !email || !password || !cpassword || !dob || !country || !gender){ ","            $(\"#msgDiv\").show().html(\"All fields are required.\");","        } else if(cpassword != password){","            $(\"#msgDiv\").show().html(\"Passowrds should match.\");","        } else if (!terms){","            $(\"#msgDiv\").show().html(\"Please agree to terms and conditions.\");","        }","        else{ ","            $.ajax({","                url: \"/register\",","                method: \"POST\",","                data: { full_name: fullname, email: email, password: password, cpassword: cpassword, dob: dob, country: country, gender: gender, calorie:calorie ,salt: salt, terms: terms }","            }).done(function( data ) {","                if ( data ) {","                    if(data.status == 'error'){","                        var errors = '<ul>';","                        $.each( data.message, function( key, value ) {","                            errors = errors +'<li>'+value.msg+'</li>';","                        });","                        errors = errors+ '</ul>';","                        $(\"#msgDiv\").html(errors).show();","                    }else{","                        $(\"#msgDiv\").removeClass('alert-danger').addClass('alert-success').html(data.message).show(); ","                    }","                }","            });","        }","    });","});"],"id":1}],[{"start":{"row":6,"column":8},"end":{"row":12,"column":64},"action":"remove","lines":["var cpassword  = $(\"#cpassword\").val();","        var dob        = $(\"#dob\").val();","        var country    = $(\"#country\").val();","        var gender     = $('input[name=\"gender\"]:checked').val(); ","        var calorie    = $('input[name=\"calorie\"]:checked').val(); ","        var salt       = $('input[name=\"salt\"]:checked').val();","        var terms      = $('input[name=\"terms\"]:checked').val();"],"id":2}],[{"start":{"row":3,"column":19},"end":{"row":3,"column":20},"action":"remove","lines":["e"],"id":3},{"start":{"row":3,"column":18},"end":{"row":3,"column":19},"action":"remove","lines":["m"]},{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"remove","lines":["a"]},{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"remove","lines":["n"]},{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"remove","lines":["l"]},{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"remove","lines":["l"]},{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"remove","lines":["u"]},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"remove","lines":["f"]}],[{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["u"],"id":4},{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":["s"]},{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"insert","lines":["e"]},{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"insert","lines":["r"]},{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"insert","lines":["n"]},{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"insert","lines":["a"]},{"start":{"row":3,"column":18},"end":{"row":3,"column":19},"action":"insert","lines":["m"]},{"start":{"row":3,"column":19},"end":{"row":3,"column":20},"action":"insert","lines":["e"]}],[{"start":{"row":3,"column":36},"end":{"row":3,"column":37},"action":"remove","lines":["e"],"id":5},{"start":{"row":3,"column":35},"end":{"row":3,"column":36},"action":"remove","lines":["m"]},{"start":{"row":3,"column":34},"end":{"row":3,"column":35},"action":"remove","lines":["a"]},{"start":{"row":3,"column":33},"end":{"row":3,"column":34},"action":"remove","lines":["n"]},{"start":{"row":3,"column":32},"end":{"row":3,"column":33},"action":"remove","lines":["l"]},{"start":{"row":3,"column":31},"end":{"row":3,"column":32},"action":"remove","lines":["l"]},{"start":{"row":3,"column":30},"end":{"row":3,"column":31},"action":"remove","lines":["u"]},{"start":{"row":3,"column":29},"end":{"row":3,"column":30},"action":"remove","lines":["f"]}],[{"start":{"row":3,"column":29},"end":{"row":3,"column":30},"action":"insert","lines":["u"],"id":6},{"start":{"row":3,"column":30},"end":{"row":3,"column":31},"action":"insert","lines":["s"]},{"start":{"row":3,"column":31},"end":{"row":3,"column":32},"action":"insert","lines":["e"]},{"start":{"row":3,"column":32},"end":{"row":3,"column":33},"action":"insert","lines":["r"]},{"start":{"row":3,"column":33},"end":{"row":3,"column":34},"action":"insert","lines":["n"]},{"start":{"row":3,"column":34},"end":{"row":3,"column":35},"action":"insert","lines":["a"]}],[{"start":{"row":3,"column":35},"end":{"row":3,"column":36},"action":"insert","lines":["m"],"id":7},{"start":{"row":3,"column":36},"end":{"row":3,"column":37},"action":"insert","lines":["e"]}],[{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"remove","lines":["        var email      = $(\"#email\").val();",""],"id":8}],[{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"remove","lines":["e"],"id":9},{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"remove","lines":["m"]},{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"remove","lines":["a"]},{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"remove","lines":["n"]},{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"remove","lines":["l"]},{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"remove","lines":["l"]},{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"remove","lines":["u"]},{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"remove","lines":["f"]}],[{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":["u"],"id":10},{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":["s"]},{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"insert","lines":["e"]},{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"insert","lines":["r"]},{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"insert","lines":["n"]},{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"insert","lines":["a"]},{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"insert","lines":["m"]},{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"insert","lines":["e"]}],[{"start":{"row":6,"column":29},"end":{"row":6,"column":30},"action":"remove","lines":["l"],"id":11},{"start":{"row":6,"column":28},"end":{"row":6,"column":29},"action":"remove","lines":["i"]},{"start":{"row":6,"column":27},"end":{"row":6,"column":28},"action":"remove","lines":["a"]},{"start":{"row":6,"column":26},"end":{"row":6,"column":27},"action":"remove","lines":["m"]},{"start":{"row":6,"column":25},"end":{"row":6,"column":26},"action":"remove","lines":["e"]},{"start":{"row":6,"column":24},"end":{"row":6,"column":25},"action":"remove","lines":["!"]},{"start":{"row":6,"column":23},"end":{"row":6,"column":24},"action":"remove","lines":[" "]},{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"remove","lines":["|"]},{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"remove","lines":["|"]}],[{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"remove","lines":[" "],"id":12}],[{"start":{"row":6,"column":77},"end":{"row":6,"column":78},"action":"remove","lines":["r"],"id":13},{"start":{"row":6,"column":76},"end":{"row":6,"column":77},"action":"remove","lines":["e"]},{"start":{"row":6,"column":75},"end":{"row":6,"column":76},"action":"remove","lines":["d"]},{"start":{"row":6,"column":74},"end":{"row":6,"column":75},"action":"remove","lines":["n"]},{"start":{"row":6,"column":73},"end":{"row":6,"column":74},"action":"remove","lines":["e"]},{"start":{"row":6,"column":72},"end":{"row":6,"column":73},"action":"remove","lines":["g"]},{"start":{"row":6,"column":71},"end":{"row":6,"column":72},"action":"remove","lines":["!"]},{"start":{"row":6,"column":70},"end":{"row":6,"column":71},"action":"remove","lines":[" "]},{"start":{"row":6,"column":69},"end":{"row":6,"column":70},"action":"remove","lines":["|"]},{"start":{"row":6,"column":68},"end":{"row":6,"column":69},"action":"remove","lines":["|"]},{"start":{"row":6,"column":67},"end":{"row":6,"column":68},"action":"remove","lines":[" "]},{"start":{"row":6,"column":66},"end":{"row":6,"column":67},"action":"remove","lines":["y"]},{"start":{"row":6,"column":65},"end":{"row":6,"column":66},"action":"remove","lines":["r"]},{"start":{"row":6,"column":64},"end":{"row":6,"column":65},"action":"remove","lines":["t"]},{"start":{"row":6,"column":63},"end":{"row":6,"column":64},"action":"remove","lines":["n"]},{"start":{"row":6,"column":62},"end":{"row":6,"column":63},"action":"remove","lines":["u"]},{"start":{"row":6,"column":61},"end":{"row":6,"column":62},"action":"remove","lines":["o"]},{"start":{"row":6,"column":60},"end":{"row":6,"column":61},"action":"remove","lines":["c"]},{"start":{"row":6,"column":59},"end":{"row":6,"column":60},"action":"remove","lines":["!"]},{"start":{"row":6,"column":58},"end":{"row":6,"column":59},"action":"remove","lines":[" "]},{"start":{"row":6,"column":57},"end":{"row":6,"column":58},"action":"remove","lines":["|"]},{"start":{"row":6,"column":56},"end":{"row":6,"column":57},"action":"remove","lines":["|"]},{"start":{"row":6,"column":55},"end":{"row":6,"column":56},"action":"remove","lines":[" "]},{"start":{"row":6,"column":54},"end":{"row":6,"column":55},"action":"remove","lines":["b"]},{"start":{"row":6,"column":53},"end":{"row":6,"column":54},"action":"remove","lines":["o"]},{"start":{"row":6,"column":52},"end":{"row":6,"column":53},"action":"remove","lines":["d"]},{"start":{"row":6,"column":51},"end":{"row":6,"column":52},"action":"remove","lines":["!"]},{"start":{"row":6,"column":50},"end":{"row":6,"column":51},"action":"remove","lines":[" "]},{"start":{"row":6,"column":49},"end":{"row":6,"column":50},"action":"remove","lines":["|"]},{"start":{"row":6,"column":48},"end":{"row":6,"column":49},"action":"remove","lines":["|"]},{"start":{"row":6,"column":47},"end":{"row":6,"column":48},"action":"remove","lines":[" "]},{"start":{"row":6,"column":46},"end":{"row":6,"column":47},"action":"remove","lines":["d"]},{"start":{"row":6,"column":45},"end":{"row":6,"column":46},"action":"remove","lines":["r"]},{"start":{"row":6,"column":44},"end":{"row":6,"column":45},"action":"remove","lines":["o"]},{"start":{"row":6,"column":43},"end":{"row":6,"column":44},"action":"remove","lines":["w"]},{"start":{"row":6,"column":42},"end":{"row":6,"column":43},"action":"remove","lines":["s"]},{"start":{"row":6,"column":41},"end":{"row":6,"column":42},"action":"remove","lines":["s"]}],[{"start":{"row":6,"column":40},"end":{"row":6,"column":41},"action":"remove","lines":["a"],"id":14},{"start":{"row":6,"column":39},"end":{"row":6,"column":40},"action":"remove","lines":["p"]},{"start":{"row":6,"column":38},"end":{"row":6,"column":39},"action":"remove","lines":["c"]},{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"remove","lines":["!"]},{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"remove","lines":[" "]},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"remove","lines":["|"]},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"remove","lines":["|"]},{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"remove","lines":[" "]}],[{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"insert","lines":[" "],"id":15}],[{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"insert","lines":["|"],"id":16},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"insert","lines":["|"]}],[{"start":{"row":8,"column":8},"end":{"row":9,"column":64},"action":"remove","lines":["} else if(cpassword != password){","            $(\"#msgDiv\").show().html(\"Passowrds should match.\");"],"id":17},{"start":{"row":8,"column":4},"end":{"row":8,"column":8},"action":"remove","lines":["    "]},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"remove","lines":["    "]},{"start":{"row":7,"column":65},"end":{"row":8,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":8,"column":8},"end":{"row":9,"column":78},"action":"remove","lines":["} else if (!terms){","            $(\"#msgDiv\").show().html(\"Please agree to terms and conditions.\");"],"id":18},{"start":{"row":8,"column":4},"end":{"row":8,"column":8},"action":"remove","lines":["    "]},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"remove","lines":["    "]},{"start":{"row":7,"column":65},"end":{"row":8,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":13,"column":32},"end":{"row":13,"column":33},"action":"remove","lines":["e"],"id":19},{"start":{"row":13,"column":31},"end":{"row":13,"column":32},"action":"remove","lines":["m"]},{"start":{"row":13,"column":30},"end":{"row":13,"column":31},"action":"remove","lines":["a"]},{"start":{"row":13,"column":29},"end":{"row":13,"column":30},"action":"remove","lines":["n"]},{"start":{"row":13,"column":28},"end":{"row":13,"column":29},"action":"remove","lines":["_"]},{"start":{"row":13,"column":27},"end":{"row":13,"column":28},"action":"remove","lines":["l"]},{"start":{"row":13,"column":26},"end":{"row":13,"column":27},"action":"remove","lines":["l"]},{"start":{"row":13,"column":25},"end":{"row":13,"column":26},"action":"remove","lines":["u"]},{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"remove","lines":["f"]}],[{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"insert","lines":["u"],"id":20},{"start":{"row":13,"column":25},"end":{"row":13,"column":26},"action":"insert","lines":["s"]},{"start":{"row":13,"column":26},"end":{"row":13,"column":27},"action":"insert","lines":["e"]},{"start":{"row":13,"column":27},"end":{"row":13,"column":28},"action":"insert","lines":["r"]},{"start":{"row":13,"column":28},"end":{"row":13,"column":29},"action":"insert","lines":["_"]}],[{"start":{"row":13,"column":29},"end":{"row":13,"column":30},"action":"insert","lines":["n"],"id":21},{"start":{"row":13,"column":30},"end":{"row":13,"column":31},"action":"insert","lines":["a"]},{"start":{"row":13,"column":31},"end":{"row":13,"column":32},"action":"insert","lines":["m"]},{"start":{"row":13,"column":32},"end":{"row":13,"column":33},"action":"insert","lines":["e"]}],[{"start":{"row":13,"column":42},"end":{"row":13,"column":43},"action":"remove","lines":["e"],"id":22},{"start":{"row":13,"column":41},"end":{"row":13,"column":42},"action":"remove","lines":["m"]},{"start":{"row":13,"column":40},"end":{"row":13,"column":41},"action":"remove","lines":["a"]},{"start":{"row":13,"column":39},"end":{"row":13,"column":40},"action":"remove","lines":["n"]},{"start":{"row":13,"column":38},"end":{"row":13,"column":39},"action":"remove","lines":["l"]},{"start":{"row":13,"column":37},"end":{"row":13,"column":38},"action":"remove","lines":["l"]},{"start":{"row":13,"column":36},"end":{"row":13,"column":37},"action":"remove","lines":["u"]},{"start":{"row":13,"column":35},"end":{"row":13,"column":36},"action":"remove","lines":["f"]}],[{"start":{"row":13,"column":35},"end":{"row":13,"column":36},"action":"insert","lines":["u"],"id":23},{"start":{"row":13,"column":36},"end":{"row":13,"column":37},"action":"insert","lines":["s"]},{"start":{"row":13,"column":37},"end":{"row":13,"column":38},"action":"insert","lines":["e"]},{"start":{"row":13,"column":38},"end":{"row":13,"column":39},"action":"insert","lines":["r"]},{"start":{"row":13,"column":39},"end":{"row":13,"column":40},"action":"insert","lines":["n"]},{"start":{"row":13,"column":40},"end":{"row":13,"column":41},"action":"insert","lines":["a"]},{"start":{"row":13,"column":41},"end":{"row":13,"column":42},"action":"insert","lines":["m"]},{"start":{"row":13,"column":42},"end":{"row":13,"column":43},"action":"insert","lines":["e"]}],[{"start":{"row":13,"column":45},"end":{"row":13,"column":59},"action":"remove","lines":["email: email, "],"id":24}],[{"start":{"row":13,"column":65},"end":{"row":13,"column":173},"action":"remove","lines":["cpassword: cpassword, dob: dob, country: country, gender: gender, calorie:calorie ,salt: salt, terms: terms "],"id":25},{"start":{"row":13,"column":64},"end":{"row":13,"column":65},"action":"remove","lines":[" "]}],[{"start":{"row":13,"column":64},"end":{"row":13,"column":65},"action":"insert","lines":[" "],"id":26}],[{"start":{"row":13,"column":63},"end":{"row":13,"column":64},"action":"remove","lines":[","],"id":27}],[{"start":{"row":24,"column":61},"end":{"row":24,"column":62},"action":"remove","lines":["r"],"id":28},{"start":{"row":24,"column":60},"end":{"row":24,"column":61},"action":"remove","lines":["e"]},{"start":{"row":24,"column":59},"end":{"row":24,"column":60},"action":"remove","lines":["g"]},{"start":{"row":24,"column":58},"end":{"row":24,"column":59},"action":"remove","lines":["n"]},{"start":{"row":24,"column":57},"end":{"row":24,"column":58},"action":"remove","lines":["a"]},{"start":{"row":24,"column":56},"end":{"row":24,"column":57},"action":"remove","lines":["d"]},{"start":{"row":24,"column":55},"end":{"row":24,"column":56},"action":"remove","lines":["-"]},{"start":{"row":24,"column":54},"end":{"row":24,"column":55},"action":"remove","lines":["t"]},{"start":{"row":24,"column":53},"end":{"row":24,"column":54},"action":"remove","lines":["r"]},{"start":{"row":24,"column":52},"end":{"row":24,"column":53},"action":"remove","lines":["e"]},{"start":{"row":24,"column":51},"end":{"row":24,"column":52},"action":"remove","lines":["l"]},{"start":{"row":24,"column":50},"end":{"row":24,"column":51},"action":"remove","lines":["a"]}],[{"start":{"row":24,"column":50},"end":{"row":24,"column":51},"action":"insert","lines":["i"],"id":29},{"start":{"row":24,"column":51},"end":{"row":24,"column":52},"action":"insert","lines":["n"]},{"start":{"row":24,"column":52},"end":{"row":24,"column":53},"action":"insert","lines":["v"]},{"start":{"row":24,"column":53},"end":{"row":24,"column":54},"action":"insert","lines":["a"]},{"start":{"row":24,"column":54},"end":{"row":24,"column":55},"action":"insert","lines":["l"]},{"start":{"row":24,"column":55},"end":{"row":24,"column":56},"action":"insert","lines":["i"]},{"start":{"row":24,"column":56},"end":{"row":24,"column":57},"action":"insert","lines":["d"]}],[{"start":{"row":24,"column":82},"end":{"row":24,"column":83},"action":"remove","lines":["s"],"id":30},{"start":{"row":24,"column":81},"end":{"row":24,"column":82},"action":"remove","lines":["s"]},{"start":{"row":24,"column":80},"end":{"row":24,"column":81},"action":"remove","lines":["e"]},{"start":{"row":24,"column":79},"end":{"row":24,"column":80},"action":"remove","lines":["c"]},{"start":{"row":24,"column":78},"end":{"row":24,"column":79},"action":"remove","lines":["c"]},{"start":{"row":24,"column":77},"end":{"row":24,"column":78},"action":"remove","lines":["u"]},{"start":{"row":24,"column":76},"end":{"row":24,"column":77},"action":"remove","lines":["s"]},{"start":{"row":24,"column":75},"end":{"row":24,"column":76},"action":"remove","lines":["-"]},{"start":{"row":24,"column":74},"end":{"row":24,"column":75},"action":"remove","lines":["t"]},{"start":{"row":24,"column":73},"end":{"row":24,"column":74},"action":"remove","lines":["r"]},{"start":{"row":24,"column":72},"end":{"row":24,"column":73},"action":"remove","lines":["e"]},{"start":{"row":24,"column":71},"end":{"row":24,"column":72},"action":"remove","lines":["l"]},{"start":{"row":24,"column":70},"end":{"row":24,"column":71},"action":"remove","lines":["a"]}],[{"start":{"row":24,"column":70},"end":{"row":24,"column":71},"action":"insert","lines":["v"],"id":31},{"start":{"row":24,"column":71},"end":{"row":24,"column":72},"action":"insert","lines":["a"]},{"start":{"row":24,"column":72},"end":{"row":24,"column":73},"action":"insert","lines":["l"]},{"start":{"row":24,"column":73},"end":{"row":24,"column":74},"action":"insert","lines":["i"]},{"start":{"row":24,"column":74},"end":{"row":24,"column":75},"action":"insert","lines":["d"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":24,"column":63},"end":{"row":24,"column":63},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1572838527036}