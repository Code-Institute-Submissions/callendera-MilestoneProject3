{"filter":false,"title":"recipe.py","tooltip":"/recipe.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":26,"column":35},"end":{"row":26,"column":36},"action":"insert","lines":["-"],"id":234},{"start":{"row":26,"column":36},"end":{"row":26,"column":37},"action":"insert","lines":["h"]},{"start":{"row":26,"column":37},"end":{"row":26,"column":38},"action":"insert","lines":["o"]},{"start":{"row":26,"column":38},"end":{"row":26,"column":39},"action":"insert","lines":["m"]},{"start":{"row":26,"column":39},"end":{"row":26,"column":40},"action":"insert","lines":["e"]}],[{"start":{"row":21,"column":39},"end":{"row":21,"column":40},"action":"remove","lines":["e"],"id":235},{"start":{"row":21,"column":38},"end":{"row":21,"column":39},"action":"remove","lines":["m"]},{"start":{"row":21,"column":37},"end":{"row":21,"column":38},"action":"remove","lines":["o"]},{"start":{"row":21,"column":36},"end":{"row":21,"column":37},"action":"remove","lines":["h"]}],[{"start":{"row":21,"column":36},"end":{"row":21,"column":37},"action":"insert","lines":["d"],"id":236},{"start":{"row":21,"column":37},"end":{"row":21,"column":38},"action":"insert","lines":["e"]},{"start":{"row":21,"column":38},"end":{"row":21,"column":39},"action":"insert","lines":["t"]},{"start":{"row":21,"column":39},"end":{"row":21,"column":40},"action":"insert","lines":["a"]},{"start":{"row":21,"column":40},"end":{"row":21,"column":41},"action":"insert","lines":["i"]},{"start":{"row":21,"column":41},"end":{"row":21,"column":42},"action":"insert","lines":["l"]},{"start":{"row":21,"column":42},"end":{"row":21,"column":43},"action":"insert","lines":["s"]}],[{"start":{"row":21,"column":42},"end":{"row":21,"column":43},"action":"remove","lines":["s"],"id":237},{"start":{"row":21,"column":41},"end":{"row":21,"column":42},"action":"remove","lines":["l"]},{"start":{"row":21,"column":40},"end":{"row":21,"column":41},"action":"remove","lines":["i"]},{"start":{"row":21,"column":39},"end":{"row":21,"column":40},"action":"remove","lines":["a"]},{"start":{"row":21,"column":38},"end":{"row":21,"column":39},"action":"remove","lines":["t"]},{"start":{"row":21,"column":37},"end":{"row":21,"column":38},"action":"remove","lines":["e"]},{"start":{"row":21,"column":36},"end":{"row":21,"column":37},"action":"remove","lines":["d"]}],[{"start":{"row":21,"column":36},"end":{"row":21,"column":37},"action":"insert","lines":["h"],"id":238},{"start":{"row":21,"column":37},"end":{"row":21,"column":38},"action":"insert","lines":["o"]},{"start":{"row":21,"column":38},"end":{"row":21,"column":39},"action":"insert","lines":["m"]},{"start":{"row":21,"column":39},"end":{"row":21,"column":40},"action":"insert","lines":["e"]}],[{"start":{"row":32,"column":43},"end":{"row":33,"column":0},"action":"insert","lines":["",""],"id":239},{"start":{"row":33,"column":0},"end":{"row":33,"column":4},"action":"insert","lines":["    "]},{"start":{"row":33,"column":4},"end":{"row":34,"column":0},"action":"insert","lines":["",""]},{"start":{"row":34,"column":0},"end":{"row":34,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":34,"column":0},"end":{"row":34,"column":4},"action":"remove","lines":["    "],"id":240}],[{"start":{"row":34,"column":0},"end":{"row":43,"column":0},"action":"insert","lines":["@app.route('/view_recipe/<recipe_id>')","def view_recipe(recipe_id):","    recipe = mongo.db.recipes","    recipe.find_one_and_update(","        {'_id': ObjectId(recipe_id)},","        {'$inc': {'views': 1}}","    )","    recipe_db = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})","    return render_template(\"viewrecipe.html\", recipe=recipe_db)",""],"id":241}],[{"start":{"row":34,"column":0},"end":{"row":34,"column":2},"action":"insert","lines":["# "],"id":242},{"start":{"row":35,"column":0},"end":{"row":35,"column":2},"action":"insert","lines":["# "]},{"start":{"row":36,"column":0},"end":{"row":36,"column":2},"action":"insert","lines":["# "]},{"start":{"row":37,"column":0},"end":{"row":37,"column":2},"action":"insert","lines":["# "]},{"start":{"row":38,"column":0},"end":{"row":38,"column":2},"action":"insert","lines":["# "]},{"start":{"row":39,"column":0},"end":{"row":39,"column":2},"action":"insert","lines":["# "]},{"start":{"row":40,"column":0},"end":{"row":40,"column":2},"action":"insert","lines":["# "]},{"start":{"row":41,"column":0},"end":{"row":41,"column":2},"action":"insert","lines":["# "]},{"start":{"row":42,"column":0},"end":{"row":42,"column":2},"action":"insert","lines":["# "]}],[{"start":{"row":37,"column":33},"end":{"row":37,"column":34},"action":"insert","lines":["s"],"id":243}],[{"start":{"row":34,"column":0},"end":{"row":34,"column":2},"action":"remove","lines":["# "],"id":244},{"start":{"row":35,"column":0},"end":{"row":35,"column":2},"action":"remove","lines":["# "]},{"start":{"row":36,"column":0},"end":{"row":36,"column":2},"action":"remove","lines":["# "]},{"start":{"row":37,"column":0},"end":{"row":37,"column":2},"action":"remove","lines":["# "]},{"start":{"row":38,"column":0},"end":{"row":38,"column":2},"action":"remove","lines":["# "]},{"start":{"row":39,"column":0},"end":{"row":39,"column":2},"action":"remove","lines":["# "]},{"start":{"row":40,"column":0},"end":{"row":40,"column":2},"action":"remove","lines":["# "]},{"start":{"row":41,"column":0},"end":{"row":41,"column":2},"action":"remove","lines":["# "]},{"start":{"row":42,"column":0},"end":{"row":42,"column":2},"action":"remove","lines":["# "]}],[{"start":{"row":38,"column":25},"end":{"row":38,"column":26},"action":"insert","lines":["<"],"id":245}],[{"start":{"row":38,"column":35},"end":{"row":38,"column":36},"action":"insert","lines":[">"],"id":246}],[{"start":{"row":38,"column":36},"end":{"row":38,"column":38},"action":"insert","lines":["''"],"id":247}],[{"start":{"row":38,"column":36},"end":{"row":38,"column":38},"action":"remove","lines":["''"],"id":248}],[{"start":{"row":38,"column":25},"end":{"row":38,"column":26},"action":"insert","lines":["'"],"id":249}],[{"start":{"row":38,"column":37},"end":{"row":38,"column":38},"action":"insert","lines":["'"],"id":250}],[{"start":{"row":38,"column":37},"end":{"row":38,"column":38},"action":"remove","lines":["'"],"id":251}],[{"start":{"row":38,"column":25},"end":{"row":38,"column":26},"action":"remove","lines":["'"],"id":252}],[{"start":{"row":38,"column":25},"end":{"row":38,"column":26},"action":"remove","lines":["<"],"id":253}],[{"start":{"row":38,"column":34},"end":{"row":38,"column":35},"action":"remove","lines":[">"],"id":254}],[{"start":{"row":38,"column":35},"end":{"row":38,"column":36},"action":"remove","lines":["}"],"id":255}],[{"start":{"row":38,"column":8},"end":{"row":38,"column":9},"action":"remove","lines":["{"],"id":256}],[{"start":{"row":39,"column":29},"end":{"row":39,"column":30},"action":"remove","lines":["}"],"id":257},{"start":{"row":39,"column":28},"end":{"row":39,"column":29},"action":"remove","lines":["}"]},{"start":{"row":39,"column":27},"end":{"row":39,"column":28},"action":"remove","lines":["1"]},{"start":{"row":39,"column":26},"end":{"row":39,"column":27},"action":"remove","lines":[" "]},{"start":{"row":39,"column":25},"end":{"row":39,"column":26},"action":"remove","lines":[":"]},{"start":{"row":39,"column":24},"end":{"row":39,"column":25},"action":"remove","lines":["'"]},{"start":{"row":39,"column":23},"end":{"row":39,"column":24},"action":"remove","lines":["s"]},{"start":{"row":39,"column":22},"end":{"row":39,"column":23},"action":"remove","lines":["w"]},{"start":{"row":39,"column":21},"end":{"row":39,"column":22},"action":"remove","lines":["e"]},{"start":{"row":39,"column":20},"end":{"row":39,"column":21},"action":"remove","lines":["i"]},{"start":{"row":39,"column":19},"end":{"row":39,"column":20},"action":"remove","lines":["v"]},{"start":{"row":39,"column":18},"end":{"row":39,"column":19},"action":"remove","lines":["'"]}],[{"start":{"row":39,"column":17},"end":{"row":39,"column":18},"action":"remove","lines":["{"],"id":258},{"start":{"row":39,"column":16},"end":{"row":39,"column":17},"action":"remove","lines":[" "]},{"start":{"row":39,"column":15},"end":{"row":39,"column":16},"action":"remove","lines":[":"]},{"start":{"row":39,"column":14},"end":{"row":39,"column":15},"action":"remove","lines":["'"]},{"start":{"row":39,"column":13},"end":{"row":39,"column":14},"action":"remove","lines":["c"]},{"start":{"row":39,"column":12},"end":{"row":39,"column":13},"action":"remove","lines":["n"]},{"start":{"row":39,"column":11},"end":{"row":39,"column":12},"action":"remove","lines":["i"]},{"start":{"row":39,"column":10},"end":{"row":39,"column":11},"action":"remove","lines":["$"]},{"start":{"row":39,"column":9},"end":{"row":39,"column":10},"action":"remove","lines":["'"]},{"start":{"row":39,"column":8},"end":{"row":39,"column":9},"action":"remove","lines":["{"]},{"start":{"row":39,"column":4},"end":{"row":39,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"remove","lines":["    "],"id":259},{"start":{"row":38,"column":35},"end":{"row":39,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":38,"column":34},"end":{"row":38,"column":35},"action":"insert","lines":["}"],"id":260}],[{"start":{"row":38,"column":8},"end":{"row":38,"column":9},"action":"insert","lines":["{"],"id":261}],[{"start":{"row":41,"column":37},"end":{"row":41,"column":38},"action":"remove","lines":["e"],"id":262},{"start":{"row":41,"column":36},"end":{"row":41,"column":37},"action":"remove","lines":["p"]},{"start":{"row":41,"column":35},"end":{"row":41,"column":36},"action":"remove","lines":["i"]},{"start":{"row":41,"column":34},"end":{"row":41,"column":35},"action":"remove","lines":["c"]},{"start":{"row":41,"column":33},"end":{"row":41,"column":34},"action":"remove","lines":["e"]},{"start":{"row":41,"column":32},"end":{"row":41,"column":33},"action":"remove","lines":["r"]},{"start":{"row":41,"column":31},"end":{"row":41,"column":32},"action":"remove","lines":["w"]},{"start":{"row":41,"column":30},"end":{"row":41,"column":31},"action":"remove","lines":["e"]},{"start":{"row":41,"column":29},"end":{"row":41,"column":30},"action":"remove","lines":["i"]},{"start":{"row":41,"column":28},"end":{"row":41,"column":29},"action":"remove","lines":["v"]}],[{"start":{"row":41,"column":28},"end":{"row":41,"column":29},"action":"insert","lines":["r"],"id":263},{"start":{"row":41,"column":29},"end":{"row":41,"column":30},"action":"insert","lines":["e"]},{"start":{"row":41,"column":30},"end":{"row":41,"column":31},"action":"insert","lines":["c"]},{"start":{"row":41,"column":31},"end":{"row":41,"column":32},"action":"insert","lines":["i"]},{"start":{"row":41,"column":32},"end":{"row":41,"column":33},"action":"insert","lines":["p"]},{"start":{"row":41,"column":33},"end":{"row":41,"column":34},"action":"insert","lines":["e"]}],[{"start":{"row":41,"column":34},"end":{"row":41,"column":35},"action":"insert","lines":["-"],"id":264},{"start":{"row":41,"column":35},"end":{"row":41,"column":36},"action":"insert","lines":["d"]},{"start":{"row":41,"column":36},"end":{"row":41,"column":37},"action":"insert","lines":["e"]},{"start":{"row":41,"column":37},"end":{"row":41,"column":38},"action":"insert","lines":["t"]},{"start":{"row":41,"column":38},"end":{"row":41,"column":39},"action":"insert","lines":["a"]},{"start":{"row":41,"column":39},"end":{"row":41,"column":40},"action":"insert","lines":["i"]},{"start":{"row":41,"column":40},"end":{"row":41,"column":41},"action":"insert","lines":["l"]}],[{"start":{"row":41,"column":41},"end":{"row":41,"column":42},"action":"insert","lines":["s"],"id":265}],[{"start":{"row":42,"column":0},"end":{"row":42,"column":2},"action":"insert","lines":["# "],"id":266}],[{"start":{"row":42,"column":1},"end":{"row":42,"column":2},"action":"remove","lines":[" "],"id":267},{"start":{"row":42,"column":0},"end":{"row":42,"column":1},"action":"remove","lines":["#"]}],[{"start":{"row":34,"column":0},"end":{"row":34,"column":2},"action":"insert","lines":["# "],"id":268},{"start":{"row":35,"column":0},"end":{"row":35,"column":2},"action":"insert","lines":["# "]},{"start":{"row":36,"column":0},"end":{"row":36,"column":2},"action":"insert","lines":["# "]},{"start":{"row":37,"column":0},"end":{"row":37,"column":2},"action":"insert","lines":["# "]},{"start":{"row":38,"column":0},"end":{"row":38,"column":2},"action":"insert","lines":["# "]},{"start":{"row":39,"column":0},"end":{"row":39,"column":2},"action":"insert","lines":["# "]},{"start":{"row":40,"column":0},"end":{"row":40,"column":2},"action":"insert","lines":["# "]},{"start":{"row":41,"column":0},"end":{"row":41,"column":2},"action":"insert","lines":["# "]}],[{"start":{"row":34,"column":0},"end":{"row":42,"column":0},"action":"remove","lines":["# @app.route('/view_recipe/<recipe_id>')","# def view_recipe(recipe_id):","#     recipe = mongo.db.recipes","#     recipe.find_one_and_update(s","#         {'_id': ObjectId(recipe_id)},","#     )","#     recipe_db = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})","#     return render_template(\"recipe-details.html\", recipe=recipe_db)",""],"id":269}],[{"start":{"row":34,"column":0},"end":{"row":34,"column":1},"action":"insert","lines":["@"],"id":270},{"start":{"row":34,"column":1},"end":{"row":34,"column":2},"action":"insert","lines":["a"]},{"start":{"row":34,"column":2},"end":{"row":34,"column":3},"action":"insert","lines":["p"]},{"start":{"row":34,"column":3},"end":{"row":34,"column":4},"action":"insert","lines":["p"]}],[{"start":{"row":34,"column":4},"end":{"row":34,"column":5},"action":"insert","lines":["."],"id":271},{"start":{"row":34,"column":5},"end":{"row":34,"column":6},"action":"insert","lines":["r"]},{"start":{"row":34,"column":6},"end":{"row":34,"column":7},"action":"insert","lines":["o"]},{"start":{"row":34,"column":7},"end":{"row":34,"column":8},"action":"insert","lines":["u"]},{"start":{"row":34,"column":8},"end":{"row":34,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":34,"column":9},"end":{"row":34,"column":10},"action":"insert","lines":["e"],"id":272}],[{"start":{"row":34,"column":10},"end":{"row":34,"column":12},"action":"insert","lines":["()"],"id":273}],[{"start":{"row":34,"column":11},"end":{"row":34,"column":13},"action":"insert","lines":["''"],"id":274}],[{"start":{"row":34,"column":12},"end":{"row":34,"column":13},"action":"insert","lines":["/"],"id":275},{"start":{"row":34,"column":13},"end":{"row":34,"column":14},"action":"insert","lines":["s"]},{"start":{"row":34,"column":14},"end":{"row":34,"column":15},"action":"insert","lines":["i"]},{"start":{"row":34,"column":15},"end":{"row":34,"column":16},"action":"insert","lines":["n"]},{"start":{"row":34,"column":16},"end":{"row":34,"column":17},"action":"insert","lines":["g"]},{"start":{"row":34,"column":17},"end":{"row":34,"column":18},"action":"insert","lines":["l"]},{"start":{"row":34,"column":18},"end":{"row":34,"column":19},"action":"insert","lines":["e"]}],[{"start":{"row":34,"column":19},"end":{"row":34,"column":20},"action":"insert","lines":["_"],"id":276},{"start":{"row":34,"column":20},"end":{"row":34,"column":21},"action":"insert","lines":["r"]},{"start":{"row":34,"column":21},"end":{"row":34,"column":22},"action":"insert","lines":["e"]},{"start":{"row":34,"column":22},"end":{"row":34,"column":23},"action":"insert","lines":["c"]},{"start":{"row":34,"column":23},"end":{"row":34,"column":24},"action":"insert","lines":["i"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"insert","lines":["p"]},{"start":{"row":34,"column":25},"end":{"row":34,"column":26},"action":"insert","lines":["e"]}],[{"start":{"row":34,"column":26},"end":{"row":34,"column":27},"action":"insert","lines":["/"],"id":277}],[{"start":{"row":34,"column":27},"end":{"row":34,"column":28},"action":"insert","lines":["<"],"id":278},{"start":{"row":34,"column":28},"end":{"row":34,"column":29},"action":"insert","lines":["r"]},{"start":{"row":34,"column":29},"end":{"row":34,"column":30},"action":"insert","lines":["e"]},{"start":{"row":34,"column":30},"end":{"row":34,"column":31},"action":"insert","lines":["c"]},{"start":{"row":34,"column":31},"end":{"row":34,"column":32},"action":"insert","lines":["i"]},{"start":{"row":34,"column":32},"end":{"row":34,"column":33},"action":"insert","lines":["p"]},{"start":{"row":34,"column":33},"end":{"row":34,"column":34},"action":"insert","lines":["e"]}],[{"start":{"row":34,"column":34},"end":{"row":34,"column":35},"action":"insert","lines":["_"],"id":279},{"start":{"row":34,"column":35},"end":{"row":34,"column":36},"action":"insert","lines":["i"]},{"start":{"row":34,"column":36},"end":{"row":34,"column":37},"action":"insert","lines":["d"]}],[{"start":{"row":34,"column":37},"end":{"row":34,"column":38},"action":"insert","lines":[">"],"id":280}],[{"start":{"row":34,"column":40},"end":{"row":35,"column":0},"action":"insert","lines":["",""],"id":281}],[{"start":{"row":35,"column":0},"end":{"row":35,"column":1},"action":"insert","lines":["d"],"id":282},{"start":{"row":35,"column":1},"end":{"row":35,"column":2},"action":"insert","lines":["e"]},{"start":{"row":35,"column":2},"end":{"row":35,"column":3},"action":"insert","lines":["f"]}],[{"start":{"row":35,"column":3},"end":{"row":35,"column":4},"action":"insert","lines":[" "],"id":283},{"start":{"row":35,"column":4},"end":{"row":35,"column":5},"action":"insert","lines":["s"]}],[{"start":{"row":35,"column":4},"end":{"row":35,"column":5},"action":"remove","lines":["s"],"id":284}],[{"start":{"row":34,"column":18},"end":{"row":34,"column":19},"action":"remove","lines":["e"],"id":285},{"start":{"row":34,"column":17},"end":{"row":34,"column":18},"action":"remove","lines":["l"]},{"start":{"row":34,"column":16},"end":{"row":34,"column":17},"action":"remove","lines":["g"]},{"start":{"row":34,"column":15},"end":{"row":34,"column":16},"action":"remove","lines":["n"]},{"start":{"row":34,"column":14},"end":{"row":34,"column":15},"action":"remove","lines":["i"]},{"start":{"row":34,"column":13},"end":{"row":34,"column":14},"action":"remove","lines":["s"]}],[{"start":{"row":34,"column":13},"end":{"row":34,"column":14},"action":"insert","lines":["v"],"id":286},{"start":{"row":34,"column":14},"end":{"row":34,"column":15},"action":"insert","lines":["i"]},{"start":{"row":34,"column":15},"end":{"row":34,"column":16},"action":"insert","lines":["e"]},{"start":{"row":34,"column":16},"end":{"row":34,"column":17},"action":"insert","lines":["w"]}],[{"start":{"row":35,"column":4},"end":{"row":35,"column":5},"action":"insert","lines":["v"],"id":287},{"start":{"row":35,"column":5},"end":{"row":35,"column":6},"action":"insert","lines":["i"]},{"start":{"row":35,"column":6},"end":{"row":35,"column":7},"action":"insert","lines":["e"]},{"start":{"row":35,"column":7},"end":{"row":35,"column":8},"action":"insert","lines":["w"]}],[{"start":{"row":35,"column":8},"end":{"row":35,"column":9},"action":"insert","lines":["_"],"id":288},{"start":{"row":35,"column":9},"end":{"row":35,"column":10},"action":"insert","lines":["r"]},{"start":{"row":35,"column":10},"end":{"row":35,"column":11},"action":"insert","lines":["e"]},{"start":{"row":35,"column":11},"end":{"row":35,"column":12},"action":"insert","lines":["c"]},{"start":{"row":35,"column":12},"end":{"row":35,"column":13},"action":"insert","lines":["i"]},{"start":{"row":35,"column":13},"end":{"row":35,"column":14},"action":"insert","lines":["p"]},{"start":{"row":35,"column":14},"end":{"row":35,"column":15},"action":"insert","lines":["e"]}],[{"start":{"row":35,"column":15},"end":{"row":35,"column":17},"action":"insert","lines":["()"],"id":289}],[{"start":{"row":35,"column":16},"end":{"row":35,"column":17},"action":"insert","lines":["r"],"id":290},{"start":{"row":35,"column":17},"end":{"row":35,"column":18},"action":"insert","lines":["e"]},{"start":{"row":35,"column":18},"end":{"row":35,"column":19},"action":"insert","lines":["c"]},{"start":{"row":35,"column":19},"end":{"row":35,"column":20},"action":"insert","lines":["i"]},{"start":{"row":35,"column":20},"end":{"row":35,"column":21},"action":"insert","lines":["p"]},{"start":{"row":35,"column":21},"end":{"row":35,"column":22},"action":"insert","lines":["e"]}],[{"start":{"row":35,"column":22},"end":{"row":35,"column":23},"action":"insert","lines":["_"],"id":291},{"start":{"row":35,"column":23},"end":{"row":35,"column":24},"action":"insert","lines":["i"]},{"start":{"row":35,"column":24},"end":{"row":35,"column":25},"action":"insert","lines":["d"]}],[{"start":{"row":35,"column":26},"end":{"row":35,"column":27},"action":"insert","lines":[":"],"id":292}],[{"start":{"row":35,"column":27},"end":{"row":36,"column":0},"action":"insert","lines":["",""],"id":293},{"start":{"row":36,"column":0},"end":{"row":36,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":36,"column":4},"end":{"row":36,"column":5},"action":"insert","lines":["r"],"id":294},{"start":{"row":36,"column":5},"end":{"row":36,"column":6},"action":"insert","lines":["e"]},{"start":{"row":36,"column":6},"end":{"row":36,"column":7},"action":"insert","lines":["t"]},{"start":{"row":36,"column":7},"end":{"row":36,"column":8},"action":"insert","lines":["u"]},{"start":{"row":36,"column":8},"end":{"row":36,"column":9},"action":"insert","lines":["r"]},{"start":{"row":36,"column":9},"end":{"row":36,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":36,"column":10},"end":{"row":36,"column":11},"action":"insert","lines":[" "],"id":295},{"start":{"row":36,"column":11},"end":{"row":36,"column":12},"action":"insert","lines":["r"]},{"start":{"row":36,"column":12},"end":{"row":36,"column":13},"action":"insert","lines":["e"]},{"start":{"row":36,"column":13},"end":{"row":36,"column":14},"action":"insert","lines":["n"]},{"start":{"row":36,"column":14},"end":{"row":36,"column":15},"action":"insert","lines":["d"]},{"start":{"row":36,"column":15},"end":{"row":36,"column":16},"action":"insert","lines":["e"]},{"start":{"row":36,"column":16},"end":{"row":36,"column":17},"action":"insert","lines":["r"]}],[{"start":{"row":36,"column":17},"end":{"row":36,"column":18},"action":"insert","lines":["_"],"id":296},{"start":{"row":36,"column":18},"end":{"row":36,"column":19},"action":"insert","lines":["t"]},{"start":{"row":36,"column":19},"end":{"row":36,"column":20},"action":"insert","lines":["e"]},{"start":{"row":36,"column":20},"end":{"row":36,"column":21},"action":"insert","lines":["m"]},{"start":{"row":36,"column":21},"end":{"row":36,"column":22},"action":"insert","lines":["p"]},{"start":{"row":36,"column":22},"end":{"row":36,"column":23},"action":"insert","lines":["l"]},{"start":{"row":36,"column":23},"end":{"row":36,"column":24},"action":"insert","lines":["a"]},{"start":{"row":36,"column":24},"end":{"row":36,"column":25},"action":"insert","lines":["t"]},{"start":{"row":36,"column":25},"end":{"row":36,"column":26},"action":"insert","lines":["e"]}],[{"start":{"row":36,"column":26},"end":{"row":36,"column":28},"action":"insert","lines":["()"],"id":297}],[{"start":{"row":36,"column":27},"end":{"row":36,"column":29},"action":"insert","lines":["''"],"id":298}],[{"start":{"row":36,"column":28},"end":{"row":36,"column":29},"action":"insert","lines":["s"],"id":299},{"start":{"row":36,"column":29},"end":{"row":36,"column":30},"action":"insert","lines":["i"]},{"start":{"row":36,"column":30},"end":{"row":36,"column":31},"action":"insert","lines":["n"]},{"start":{"row":36,"column":31},"end":{"row":36,"column":32},"action":"insert","lines":["g"]},{"start":{"row":36,"column":32},"end":{"row":36,"column":33},"action":"insert","lines":["l"]},{"start":{"row":36,"column":33},"end":{"row":36,"column":34},"action":"insert","lines":["e"]}],[{"start":{"row":36,"column":34},"end":{"row":36,"column":35},"action":"insert","lines":["_"],"id":300},{"start":{"row":36,"column":35},"end":{"row":36,"column":36},"action":"insert","lines":["r"]},{"start":{"row":36,"column":36},"end":{"row":36,"column":37},"action":"insert","lines":["e"]},{"start":{"row":36,"column":37},"end":{"row":36,"column":38},"action":"insert","lines":["c"]},{"start":{"row":36,"column":38},"end":{"row":36,"column":39},"action":"insert","lines":["i"]},{"start":{"row":36,"column":39},"end":{"row":36,"column":40},"action":"insert","lines":["p"]},{"start":{"row":36,"column":40},"end":{"row":36,"column":41},"action":"insert","lines":["e"]}],[{"start":{"row":36,"column":40},"end":{"row":36,"column":41},"action":"remove","lines":["e"],"id":301},{"start":{"row":36,"column":39},"end":{"row":36,"column":40},"action":"remove","lines":["p"]},{"start":{"row":36,"column":38},"end":{"row":36,"column":39},"action":"remove","lines":["i"]},{"start":{"row":36,"column":37},"end":{"row":36,"column":38},"action":"remove","lines":["c"]},{"start":{"row":36,"column":36},"end":{"row":36,"column":37},"action":"remove","lines":["e"]},{"start":{"row":36,"column":35},"end":{"row":36,"column":36},"action":"remove","lines":["r"]},{"start":{"row":36,"column":34},"end":{"row":36,"column":35},"action":"remove","lines":["_"]},{"start":{"row":36,"column":33},"end":{"row":36,"column":34},"action":"remove","lines":["e"]},{"start":{"row":36,"column":32},"end":{"row":36,"column":33},"action":"remove","lines":["l"]},{"start":{"row":36,"column":31},"end":{"row":36,"column":32},"action":"remove","lines":["g"]},{"start":{"row":36,"column":30},"end":{"row":36,"column":31},"action":"remove","lines":["n"]},{"start":{"row":36,"column":29},"end":{"row":36,"column":30},"action":"remove","lines":["i"]}],[{"start":{"row":36,"column":28},"end":{"row":36,"column":29},"action":"remove","lines":["s"],"id":302}],[{"start":{"row":36,"column":28},"end":{"row":36,"column":29},"action":"insert","lines":["r"],"id":303},{"start":{"row":36,"column":29},"end":{"row":36,"column":30},"action":"insert","lines":["e"]},{"start":{"row":36,"column":30},"end":{"row":36,"column":31},"action":"insert","lines":["c"]},{"start":{"row":36,"column":31},"end":{"row":36,"column":32},"action":"insert","lines":["p"]},{"start":{"row":36,"column":32},"end":{"row":36,"column":33},"action":"insert","lines":["e"]}],[{"start":{"row":36,"column":32},"end":{"row":36,"column":33},"action":"remove","lines":["e"],"id":304},{"start":{"row":36,"column":31},"end":{"row":36,"column":32},"action":"remove","lines":["p"]}],[{"start":{"row":36,"column":31},"end":{"row":36,"column":32},"action":"insert","lines":["i"],"id":305},{"start":{"row":36,"column":32},"end":{"row":36,"column":33},"action":"insert","lines":["p"]},{"start":{"row":36,"column":33},"end":{"row":36,"column":34},"action":"insert","lines":["e"]},{"start":{"row":36,"column":34},"end":{"row":36,"column":35},"action":"insert","lines":["-"]},{"start":{"row":36,"column":35},"end":{"row":36,"column":36},"action":"insert","lines":["d"]},{"start":{"row":36,"column":36},"end":{"row":36,"column":37},"action":"insert","lines":["e"]}],[{"start":{"row":36,"column":37},"end":{"row":36,"column":38},"action":"insert","lines":["t"],"id":306},{"start":{"row":36,"column":38},"end":{"row":36,"column":39},"action":"insert","lines":["a"]},{"start":{"row":36,"column":39},"end":{"row":36,"column":40},"action":"insert","lines":["i"]},{"start":{"row":36,"column":40},"end":{"row":36,"column":41},"action":"insert","lines":["l"]}],[{"start":{"row":36,"column":41},"end":{"row":36,"column":42},"action":"insert","lines":["s"],"id":307}],[{"start":{"row":36,"column":42},"end":{"row":36,"column":43},"action":"insert","lines":["."],"id":308},{"start":{"row":36,"column":43},"end":{"row":36,"column":44},"action":"insert","lines":["h"]},{"start":{"row":36,"column":44},"end":{"row":36,"column":45},"action":"insert","lines":["t"]},{"start":{"row":36,"column":45},"end":{"row":36,"column":46},"action":"insert","lines":["m"]},{"start":{"row":36,"column":46},"end":{"row":36,"column":47},"action":"insert","lines":["l"]}],[{"start":{"row":36,"column":48},"end":{"row":36,"column":49},"action":"insert","lines":[","],"id":309}],[{"start":{"row":36,"column":49},"end":{"row":36,"column":50},"action":"insert","lines":[" "],"id":310},{"start":{"row":36,"column":50},"end":{"row":36,"column":51},"action":"insert","lines":["r"]},{"start":{"row":36,"column":51},"end":{"row":36,"column":52},"action":"insert","lines":["e"]},{"start":{"row":36,"column":52},"end":{"row":36,"column":53},"action":"insert","lines":["i"]},{"start":{"row":36,"column":53},"end":{"row":36,"column":54},"action":"insert","lines":["p"]},{"start":{"row":36,"column":54},"end":{"row":36,"column":55},"action":"insert","lines":["e"]}],[{"start":{"row":36,"column":55},"end":{"row":36,"column":56},"action":"insert","lines":["s"],"id":311}],[{"start":{"row":36,"column":55},"end":{"row":36,"column":56},"action":"remove","lines":["s"],"id":312},{"start":{"row":36,"column":54},"end":{"row":36,"column":55},"action":"remove","lines":["e"]},{"start":{"row":36,"column":53},"end":{"row":36,"column":54},"action":"remove","lines":["p"]},{"start":{"row":36,"column":52},"end":{"row":36,"column":53},"action":"remove","lines":["i"]}],[{"start":{"row":36,"column":52},"end":{"row":36,"column":53},"action":"insert","lines":["c"],"id":313},{"start":{"row":36,"column":53},"end":{"row":36,"column":54},"action":"insert","lines":["i"]},{"start":{"row":36,"column":54},"end":{"row":36,"column":55},"action":"insert","lines":["p"]},{"start":{"row":36,"column":55},"end":{"row":36,"column":56},"action":"insert","lines":["e"]},{"start":{"row":36,"column":56},"end":{"row":36,"column":57},"action":"insert","lines":["s"]}],[{"start":{"row":36,"column":57},"end":{"row":36,"column":58},"action":"insert","lines":["="],"id":314},{"start":{"row":36,"column":58},"end":{"row":36,"column":59},"action":"insert","lines":["m"]},{"start":{"row":36,"column":59},"end":{"row":36,"column":60},"action":"insert","lines":["o"]},{"start":{"row":36,"column":60},"end":{"row":36,"column":61},"action":"insert","lines":["n"]},{"start":{"row":36,"column":61},"end":{"row":36,"column":62},"action":"insert","lines":["g"]},{"start":{"row":36,"column":62},"end":{"row":36,"column":63},"action":"insert","lines":["o"]}],[{"start":{"row":36,"column":63},"end":{"row":36,"column":64},"action":"insert","lines":["."],"id":315},{"start":{"row":36,"column":64},"end":{"row":36,"column":65},"action":"insert","lines":["d"]},{"start":{"row":36,"column":65},"end":{"row":36,"column":66},"action":"insert","lines":["b"]}],[{"start":{"row":36,"column":66},"end":{"row":36,"column":67},"action":"insert","lines":["."],"id":316},{"start":{"row":36,"column":67},"end":{"row":36,"column":68},"action":"insert","lines":["r"]},{"start":{"row":36,"column":68},"end":{"row":36,"column":69},"action":"insert","lines":["e"]},{"start":{"row":36,"column":69},"end":{"row":36,"column":70},"action":"insert","lines":["c"]}],[{"start":{"row":36,"column":70},"end":{"row":36,"column":71},"action":"insert","lines":["i"],"id":317},{"start":{"row":36,"column":71},"end":{"row":36,"column":72},"action":"insert","lines":["p"]},{"start":{"row":36,"column":72},"end":{"row":36,"column":73},"action":"insert","lines":["e"]},{"start":{"row":36,"column":73},"end":{"row":36,"column":74},"action":"insert","lines":["s"]}],[{"start":{"row":36,"column":74},"end":{"row":36,"column":75},"action":"insert","lines":["."],"id":318},{"start":{"row":36,"column":75},"end":{"row":36,"column":76},"action":"insert","lines":["f"]},{"start":{"row":36,"column":76},"end":{"row":36,"column":77},"action":"insert","lines":["i"]},{"start":{"row":36,"column":77},"end":{"row":36,"column":78},"action":"insert","lines":["n"]},{"start":{"row":36,"column":78},"end":{"row":36,"column":79},"action":"insert","lines":["d"]}],[{"start":{"row":36,"column":79},"end":{"row":36,"column":81},"action":"insert","lines":["()"],"id":319}],[{"start":{"row":36,"column":80},"end":{"row":36,"column":82},"action":"insert","lines":["{}"],"id":320}],[{"start":{"row":36,"column":81},"end":{"row":36,"column":83},"action":"insert","lines":["''"],"id":321}],[{"start":{"row":36,"column":82},"end":{"row":36,"column":83},"action":"insert","lines":["_"],"id":322},{"start":{"row":36,"column":83},"end":{"row":36,"column":84},"action":"insert","lines":["i"]},{"start":{"row":36,"column":84},"end":{"row":36,"column":85},"action":"insert","lines":["d"]}],[{"start":{"row":36,"column":86},"end":{"row":36,"column":87},"action":"insert","lines":[":"],"id":323}],[{"start":{"row":36,"column":87},"end":{"row":36,"column":88},"action":"insert","lines":[" "],"id":324},{"start":{"row":36,"column":88},"end":{"row":36,"column":89},"action":"insert","lines":["O"]},{"start":{"row":36,"column":89},"end":{"row":36,"column":90},"action":"insert","lines":["b"]},{"start":{"row":36,"column":90},"end":{"row":36,"column":91},"action":"insert","lines":["j"]},{"start":{"row":36,"column":91},"end":{"row":36,"column":92},"action":"insert","lines":["e"]},{"start":{"row":36,"column":92},"end":{"row":36,"column":93},"action":"insert","lines":["c"]}],[{"start":{"row":36,"column":93},"end":{"row":36,"column":94},"action":"insert","lines":["t"],"id":325},{"start":{"row":36,"column":94},"end":{"row":36,"column":95},"action":"insert","lines":["I"]},{"start":{"row":36,"column":95},"end":{"row":36,"column":96},"action":"insert","lines":["d"]}],[{"start":{"row":36,"column":96},"end":{"row":36,"column":98},"action":"insert","lines":["()"],"id":326}],[{"start":{"row":36,"column":97},"end":{"row":36,"column":98},"action":"insert","lines":["r"],"id":327},{"start":{"row":36,"column":98},"end":{"row":36,"column":99},"action":"insert","lines":["e"]},{"start":{"row":36,"column":99},"end":{"row":36,"column":100},"action":"insert","lines":["c"]},{"start":{"row":36,"column":100},"end":{"row":36,"column":101},"action":"insert","lines":["i"]},{"start":{"row":36,"column":101},"end":{"row":36,"column":102},"action":"insert","lines":["p"]},{"start":{"row":36,"column":102},"end":{"row":36,"column":103},"action":"insert","lines":["e"]}],[{"start":{"row":36,"column":103},"end":{"row":36,"column":104},"action":"insert","lines":["_"],"id":328},{"start":{"row":36,"column":104},"end":{"row":36,"column":105},"action":"insert","lines":["i"]},{"start":{"row":36,"column":105},"end":{"row":36,"column":106},"action":"insert","lines":["d"]}],[{"start":{"row":26,"column":46},"end":{"row":26,"column":47},"action":"insert","lines":[" "],"id":329}],[{"start":{"row":26,"column":35},"end":{"row":26,"column":36},"action":"remove","lines":["-"],"id":330}],[{"start":{"row":36,"column":34},"end":{"row":36,"column":35},"action":"remove","lines":["-"],"id":331}],[{"start":{"row":21,"column":35},"end":{"row":21,"column":36},"action":"remove","lines":["-"],"id":332}],[{"start":{"row":26,"column":27},"end":{"row":26,"column":28},"action":"remove","lines":[" "],"id":333}],[{"start":{"row":26,"column":44},"end":{"row":26,"column":45},"action":"remove","lines":[" "],"id":334}]]},"ace":{"folds":[],"scrolltop":178,"scrollleft":0,"selection":{"start":{"row":26,"column":45},"end":{"row":26,"column":45},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1572877135428,"hash":"56848ffa6ea80995a7e873282fbbe70ff60dc390"}