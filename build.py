import os,json
MAP=json.load(open("assets.json"))
NAV=[("Esta Eats.","esta-eats.html"),("Lanky Design.","lanky-design.html"),("Exhibits.","exhibits.html")]
READMORE="https://www.nzherald.co.nz/hawkes-bay-today/news/fruitful-hawkes-bay-exhibition-celebrates-regions-horticultural-heritage/7UYIJL5F4FG25L6VMNBZERRP6Q/"
INSTAGRAMS=[("@fignfennel","https://instagram.com/fignfennel"),("@esta_eats","https://instagram.com/esta_eats"),("@lankydesign.nz","https://instagram.com/lankydesign.nz")]
PARENT={"exhibits.html":"index.html","esta-eats.html":"index.html","lanky-design.html":"index.html","fruitful.html":"exhibits.html","collected-by-lanky.html":"exhibits.html"}
for f in ["experiences-esta","food-communications","front-yard-forage","young-enterprise","creations-esta"]:PARENT[f+".html"]="esta-eats.html"
for f in ["experiences-jodi","auckland-design-week","look-its-lanky","lanky-kitchen","creations-jodi"]:PARENT[f+".html"]="lanky-design.html"
def page(fn,title,body,cur=""):
    back=PARENT.get(fn)
    backbtn=f'<a class="back" href="{back}"><span aria-hidden="true">&larr;</span> Back</a>' if back else '<span></span>'
    igs="".join(f'<a class="ig" href="{u}" target="_blank" rel="noopener">{n}</a>' for n,u in INSTAGRAMS)
    nav="".join(f'<a href="{h}"{" aria-current=page" if h==cur else ""}>{t}</a>' for t,h in NAV)
    html=f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | Fig n' Fennel</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css"></head><body{" class=home" if fn=="index.html" else ""}>
<header class="site-header"><a class="logo" href="index.html">FIG N' FENNEL.</a><nav class="nav" aria-label="Main">{nav}</nav></header>
<main>{body}</main>
<footer class="site-footer">{backbtn}<div class="socials">{igs}</div></footer>
<script src="script.js"></script></body></html>'''
    open(fn,"w").write(html)
STARS='<i class="star purple s1"></i><i class="star blue s2"></i><i class="star green s3"></i>'
MID='<i class="star purple hm" style="top:16%;left:55%;--s:100px"></i><i class="star blue hm" style="top:44%;left:60%;--s:80px"></i><i class="star green hm" style="top:70%;left:54%;--s:110px"></i><i class="star brown hm" style="top:90%;left:62%;--s:70px"></i>'
STORY='<i class="star purple hm" style="top:12%;left:52%;--s:100px"></i><i class="star blue hm" style="top:38%;left:55%;--s:80px"></i><i class="star green hm" style="top:62%;left:52%;--s:110px"></i><i class="star brown hm" style="top:86%;left:56%;--s:70px"></i>'
FYF='<i class="star purple hm" style="top:76%;left:54%;--s:90px"></i><i class="star green" style="bottom:3%;left:5%;--s:110px"></i><i class="star blue hm" style="bottom:6%;right:3%;--s:90px"></i>'
P=lambda t:"".join(f"<p>{x.replace(chr(10),'<br>')}</p>" for x in t.strip().split("\n\n"))
IMG=lambda n,a="":f'<img src="{MAP[n]}" alt="{a}" loading="lazy">'

# HOME
page("index.html","Home",f'''
<i class="star brown" style="top:10%;left:36%;--s:70px"></i><i class="star purple" style="top:36%;left:32%;--s:40px"></i><i class="star green" style="top:66%;left:44%;--s:60px"></i>
<section class="hero"><h1>Two<br>gals<br>with<br>many<br><em>visions.</em></h1>
<div class="art">
<i class="star blue" style="top:36%;left:28%;--s:50px"></i><i class="star green" style="top:44%;left:63%;--s:80px"></i><i class="star brown" style="bottom:6%;left:50%;--s:70px"></i>
<a href="esta-eats.html" style="top:0;left:36%;width:26%"><img src="{MAP['home-apple']}" alt="Apple core illustration"><span>Esta Eats</span></a>
<a href="exhibits.html" style="bottom:0;left:0;width:38%"><img src="{MAP['home-fennel']}" alt="Fennel and fig illustration"><span>Exhibits &amp; More</span></a>
<a href="lanky-design.html" style="top:0;right:4%;width:20%"><img src="{MAP['home-character']}" alt="Lanky character illustration"><span>Lanky Design</span></a>
</div></section>''')

# EXHIBITS
page("exhibits.html","Exhibits & More",f'''{STARS}
<div class="two"><div><h1>FIG N' FENNEL represents a collaboration<br>of two gals with many visions.</h1>{P("""Stemming from long walks after school Jodi & Esta realised not only did they love to tell stories through creativity but there were important stories to be appreciated.

Valuing sustainability through appreciation of resources, places, people and moments Fig n' Fennel exists to remind communities how special our little corner of the world is.

Below are the first of many exhibits by Fig n' Fennel following a theme of mixed mediums, interactive experiences and most importantly an appreciation for our world.

We are eager to tell more sustainable stories through immersive experiences.""")}</div>{IMG("beach","Jodi and Esta on the beach")}</div>
<div class="two" style="margin-top:3rem"><a class="frame" href="fruitful.html">{IMG("fruitful-cover","Fruitful exhibit staircase")}<h3>Fruitful.</h3></a>
<a class="frame" href="collected-by-lanky.html" style="margin-top:6rem">{IMG("collected-cover","Collected by Lanky exhibit")}<h3>Collected by Lanky.</h3></a></div>''',"exhibits.html")

# STORY PAGES
def side(items):
    return "".join(f'<figure>{IMG(i,a)}</figure><h2>{h}</h2>{P(t)}' for i,a,h,t in items)
page("fruitful.html","Fruitful",f'''{STORY}<div class="story"><div><h1>Fruitful.</h1>
<h2>Why</h2>{P("""As two fruit loving gals Fruitful was an inevitable creation but the closure of some of the Watties lines and local fruit stores replaced with chicken shops kickstarted us.
We wanted to create a world of appreciation for our place and the fruit that grows within it.""")}
<h2>What</h2>{P("Whilst searching for a place to share our story we realised the answer was already in our clutches. We knew of an Art Deco building calling to be shared with the world.")}
<figure>{IMG("fruitful-1","Refurbishing the gallery")}</figure>{P("So we started Garnett Gallery.\n\nWe then spent months refurbishing an Art Deco icon to create a place to tell our story.")}
<figure>{IMG("fruitful-2","Gallery staircase")}</figure><figure>{IMG("fruitful-3","Visitors chatting")}</figure>
<h2>Feedback.</h2>{P("""We were surprised by many of the visitors that came eager to talk about fruit. It was comforting to know we weren't the only ones with an obsession.
The exhibit brought together people willing to fly the flag of Te Matau-a-Māui as a the Fruit bowl of Aotearoa. It held a place for important conversations about the future of our region.""")}
<figure>{IMG("fruitful-4","Gallery window")}</figure><div class="last"><h2>Future Goals.</h2>{P("This event pushes us towards creating community activations. We now have a Canvas to tell important stories through art, food, and most importantly conversations. We are eager to create more worlds of important conversations because from small things big things grow.")}
<p><a href="{READMORE}" target="_blank" rel="noopener"><strong>Read more here...</strong></a></p></div></div>
<div class="right"><p class="date">July 2026.</p>
{side([("fruitful-ceramics","Lanky ceramics shelf","Lanky Ceramics.","Jodi created buttons & ceramics that serve as reminders of the brightness that fruit brings to our worlds. She also translated her work into watercolour showcasing her love for a variety of mediums."),
("fruitful-tree","The tree","The Tree!","A cardboard tree adorned with golden walnuts for visitors to pick when popping a koha into the tree for Garden to Table. Visitors walked away with a fruitful message and we lent a hand to an organisation growing our next generation of gardeners."),
("fruitful-map","Roadside stall map","Where do you stand?","An interactive map to celebrate roadside stalls. Highlighting five stalls through sketches & stories the map also included stickers for visitors to pop on their favourite produce spots. Ending the exhibit with an archive of growth in our region."),
("fruitful-wat","Visitor looking at art","WAT TIES?","We also featured Esta's mother, Shelley's work of painting which tells stories and ask's questions of 'Wat Ties?'"),
("fruitful-food","Fruitful food platter","Fruitful Food.","Esta created food to fuel happy visitors. The food was all created from locally sourced ingredients which sat alongside a map, serving as another reminder of the great things that grow here.")])}</div></div>''',"exhibits.html")

page("collected-by-lanky.html","Collected by Lanky",f'''{STORY}<div class="story"><div><h1>Collected By Lanky.</h1>
<h2>WHY</h2>{P("""After many winter walks desperate for sunshine there was one thing that always shone bright... the lemons adorning our neighbourhood trees. A brightness amongst the grey we wanted our community to appreciate.
Simultaneously Jodi jumped on an opportunity to have her first solo exhibit at Creative Arts Napier.
Collected by Lanky was born.""")}<figure>{IMG("collected-1","Jodi and Esta with lemons")}</figure>
<h2>What</h2>{P("Collected by Lanky was an exhibit of Jodi's multi disciplinary work centered on Lemons.")}<figure>{IMG("collected-2","Framed character prints")}</figure>
<figure>{IMG("collected-3","Lemon treats platter")}</figure><div class="last"><h2>The Future.</h2>{P("""This exhibit brought what were once doodles in Maths class to the community. It was incredibly satisfying to see the way visitors connected with the personality of Jodi's work.

The success of this exhibit was proof we were ready to do it all again, Fig n' Fennel was born and the journey began.""")}</div></div>
<div class="right"><p class="date">July 2025.</p>
{side([("collected-prints","Framed prints","Framed prints.","Jodi's characters representing the wild and wonderful lemons of our neighbourhoods were framed in wee prints being sure to bring joy to homes."),
("collected-buttons","Ceramic buttons","Ceramic Buttons.","Offering people an easy fix to brighten items they already own, Lanky buttons ignited creativity from visitors and continue to be popular."),
("collected-dip","Lucky dip packages","Lanky Lucky Dip.","Reminiscent of childhood lucky dips Jodi created mini one of a kind prints all wrapped in surprise. This gave visitors something small to remember their visit to the world of Lanky."),
("collected-lemonade","Lemonade pouring","Lemon Treats.","An exhibit wouldn't be complete without treats. Esta created a menu of zero waste lemon loaded goods and debuted our trademark lemon cups full of lemonade.")])}</div></div>''',"exhibits.html")

# PROFILE PAGES
def cards(c):return '<div class="cards">'+"".join(f'<a class="frame" href="{h}">{IMG(i,t)}<h3>{t}</h3><span>{d}</span></a>' for h,i,t,d in c)+'</div>'
page("esta-eats.html","Esta Eats",f'''{STARS}{MID}<div class="profile"><div><h1>Esta Eats.</h1>
<h2>Who's Esta?</h2>{P("""Esta is a gal with a whole lot of excitement for the world.
She's pretty excited to spend time experimenting in the kitchen,
Riding waves on her boogie board,
Wandering neighbourhoods foraging,
Learning lots about how to create an earth we can be proud of,

But most of all she's pretty excited to bring communities together to make change.""")}
{IMG("esta-cutout","Esta mid-leap").replace("<img","<img class=\"cutout\"")}
<h2>What's She Doing Right Now?</h2>{P("""Esta's studying a Bachelor of Design and Commerce majoring in Innovation and Entrepreneurship at the University of Auckland.

Her studies allow for lot's of agency over the content she studies so many of her projects behold food and sustainability related. She's jumped on every opportunity from classes taught by CEO's, Mentorship from a Sustainability consultant to the Deans Leadership program.

Esta loves to learn and keep busy. She heads back home to Hawkes Bay whenever she can to create with Jodi and have long walks celebrating her home.""")}
<h2>She Dabbles In.</h2>{P("Graphic Design\nPhotography and Videography\nRecipe writing\nWriting\nSewing\nEvent planning and management\nPublic Speaking\nCooking, baking & talking about food.")}
<h2>What does she care about?</h2>{P("Protecting the Whenua\n\nEating good food\n\nCreating experiences for others that are memorable, thought provoking and bring a little joy.")}
<h2>What would would she like her future to be?</h2>{P("She wants to get stuck with creating innovative solutions for our food system, solving problems with the earth in mind and bringing together people for good causes.")}
{IMG("esta-garden","Esta in a garden").replace("<img","<img style=\"max-width:300px\"")}</div>
{cards([("experiences-esta.html","esta-card-1","Experiences","Click to Read about what has shaped her"),("food-communications.html","esta-card-2","Food Communications","Check out how Esta has communicated her love for food."),("front-yard-forage.html","esta-card-3","Front Yard Forage","Read about how Esta Gathered goods for a cause."),("young-enterprise.html","esta-card-4","Young Enterprise","Esta's Young Enterprise Businesses shaped her thinking learn a little about it here."),("creations-esta.html","esta-card-5","Creations","A wee collection of fun things Esta's made.")])}</div>''',"esta-eats.html")

page("lanky-design.html","Lanky Design",f'''{STARS}{MID}<div class="profile"><div><h1>Lanky Design.</h1>
<h2>Who's Jodi?</h2>{P("""Jodi is a maker with a constantly creative outlook on life.
She seeks inspiration from the trees,
The leaves blowing in the breeze,
The patterns rippling the water's surface,
For Jodi the earth serves as her true muse.""")}
{IMG("jodi-cutout","Jodi mid-leap").replace("<img","<img class=\"cutout\"")}
<h2>What's She Doing Right Now?</h2>{P("""She's currently immersed in the world of clay, working part-time at Emily Mallard Ceramics in Napier. She creates stock for the shop whilst also helping customers along their creative journeys. Jodi enjoys the conversations and connections she's been lucky to make through this job. Otherwise she's often amidst many late night projects and seeking opportunities to learn through other's processes.""")}
<h2>She Dabbles In.</h2>{P("Working on hands on craft is her favourite form\nClay\nDrawing\nPaper craft\nSculpture\nPaper mache\nIdeation")}
<h2>What does she care about?</h2>{P("Appreciation for the world and the many great things amongst it.\nJodi has a love for fine details and an appreciation for slowing down")}
<h2>What would would she like her future to be?</h2>{P("Jodi loves to create in 3D with the earth in mind. She would enjoy exploring more ways to transform spaces to tell stories as well as creating wee reminders of the many elements of joy in our world. She would love to help others along the journey of expressing these stories through creativity.")}
{IMG("jodi-clay","Jodi working with clay").replace("<img","<img style=\"max-width:300px\"")}</div>
{cards([("experiences-jodi.html","jodi-card-1","Experiences.","Click to read about what has shaped her"),("auckland-design-week.html","jodi-card-2","Auckland Design Week.","Jodi got involved in Auckland Design Week Read about it here."),("look-its-lanky.html","jodi-card-3","Look it's Lanky!","Jodi's world on display!"),("lanky-kitchen.html","jodi-card-4","Lanky Kitchen.","Jodi created an immersive papier mache kitchen."),("creations-jodi.html","jodi-card-5","Creations","A wee collection of fun things Jodi's made.")])}</div>''',"lanky-design.html")

# DETAIL PAGES (text left, photo grid right)
def detail(fn,t,txt,n,back,sub=""):
    imgs="".join(IMG(f"{fn[:-5]}-{i+1}",f"{t} photo {i+1}") for i in range(n))
    page(fn,t,f'{STARS}<div class="detail"><div><h1>{t}</h1>{sub}{P(txt)}</div><div class="gallery">{imgs}</div></div>',back)
detail("experiences-esta.html","Experiences","""Fig n' Fennel believe there are many experiences we have been lucky to have that guide us...
Here's a few that have shaped Esta

Esta was grateful to be one of two NZ Food Communicators Scholarship recipients. This program has been full of mentorship sessions with NZ's top food writers, educators, influencers and businesses. She's created two recipes for NZ Beef and Lamb and written a story for the Outstanding Food Producers awards. This opportunity has allowed her to see how her passion for food translates into a career.

Esta started 2016 with a life changing 6 weeks in India on the Prime Minister's Scholarship for Asia study tour. The tour focussed on sustainable development, culture and bridging cross cultural connections as an ambassador for Aotearoa. The trip brought many once in a lifetime experiences but her biggest takeaway was the privilege she has to live in Aotearoa. This motivates her to protect our corner of the world and continue to learn from diverse communities.

As the daughter of a journalist and home renovator Esta has lived in a home of constant ideation. This has instilled a curiosity and love for the process of problem solving. She believes that often the answer lies in what's closest to you. She is grateful for her parents for a home that encouraged her to create curiously.""",6,"esta-eats.html")
detail("food-communications.html","Food Communications","""As a recipient of the NZ Food Communicators Scholarship Esta love's to create opportunities to share her love for food. Here is a few of them.

Greater Baker's is a monthly event held by Esta in her university hall. It brings together students eager to learn how to bake or willing to share some skills. We get together to bake a recipe and donate the goods to a charity's Kai and Connect program. The event brings together people at every stage connected to through the roots of food. This is why Esta get's immense joy from food, it brings together her other love, people. Esta would love to grow this concept beyond her hall in the future.

After making the transition moving out of home Esta realised that many University students didn't know how to have fun whilst cooking. Esta set out to change that. She creates illustrative recipe(ish)'s for the Craccum University magazine. The recipes encourage readers to swap in whatever ingredients they have on hand and relish in experimenting in the kitchen. In the future Esta would love to explore this format further and collate the recipes she has been creating.

Esta also experiments on her Instagram @estaeats. She sets herself the yearly challenge of cooking an entire cookbook a year, that's & more food moments are shared.

Good food is better shared.""",6,"esta-eats.html")
page("front-yard-forage.html","Front Yard Forage",f'''{FYF}<div class="detail"><div><p class="date" style="text-align:left">2022/23</p><h1>Front Yard Forage</h1>{P("""As an op-shopped addict Esta had created a pretty large collection of fun things that needed better homes. She found her friends with the same issue. So she thought why not bring them all together in her front yard.

She created Front Yard Forage, a one day only event bringing together her friend's second hand clothing, art and furniture to find new homes. The sale also raised funds for ReSource, a charity that rehomes goods to people in need. The event was about having a bit of summer fun and embracing the better way to buy.

This event featured a small side of Lanky Design work, the joy this work brought to people lit a wee fire in Esta's mind that she needed to bring more people together over joyful things.""")}</div><div class="gallery poster">{IMG("front-yard-forage-1","Front Yard Forage poster")}{IMG("front-yard-forage-2","Event photo")}</div></div>''',"esta-eats.html")
detail("young-enterprise.html","Young Enterprise Scheme","""As a child Esta was always dreaming up business ideas so being involved in Young Enterprise in High School was a long awaited experience. Driven by sustainability Esta created two businesses with her team focused on solving paper waste in her school.

Ours NCEA Planners
As a busy gal in High School Esta and her team saw a gap for dedicated NCEA planners, made sustainably. After many hours on Adobe Esta designed the book and it was printed on recycled paper. The planner's were well loved by many as they finally students could have a planner we could call 'Ours'.

Posie Papers
Driven to make a more direct impact on the school paper waste Esta and her team designed greeting cards made from recycled paper with native seeds embedded in the envelopes. The process of creating these cards had many prototypes, iterations and long days making paper but kickstarted Esta's love for the design process. The cards highlighted native flora and diverted paper from landfill. Esta was awarded 1st place of the regional awards and Esta was awarded national CEO of the year for her leadership.

Although Jodi wasn't a part of this team, she drew many of the pictures featured and involved in the ideation. This was planting the seed for our future of collaboration.""",4,"esta-eats.html")
def creations(fn,who,back):
    imgs="".join(IMG(f"{fn[:-5]}-{i+1}",f"Creation {i+1}") for i in range(9))
    page(fn,"Creations",f'{STARS}<p class="intro">Often it\'s the wee projects we do in our spare time that plant the seeds of bigger things<br>Here\'s a few things {who}\'s made in her time that she quite enjoys.</p><div class="gallery three">{imgs}</div>',back)
creations("creations-esta.html","Esta","esta-eats.html");creations("creations-jodi.html","Jodi","lanky-design.html")
detail("experiences-jodi.html","Experiences","""Fig n' Fennel believe there are many experiences we have been lucky to have that guide us...
Here's a few that have shaped Jodi

Jodi graduated with a Bachelor of creative practice from EIT. She knew that being a creative was the place she felt most excited by, so studying the many facets of creativity was the perfect fit. This journey allowed her to grow Lanky Design, understand the morals that guide her as well as developing tangible skills in the creative process.

Through her EIT studies she completed an internship at Emily Mallard Ceramics. This bloomed a love for clay. She also enjoyed learning about Emily's creative process as well as her way of teaching. This led to a job for Jodi after graduating which has opened her world to many more creatives.

As a child Jodi was given full creative freedom to create what was in her mind, from launching herself up a tree with a makeshift harness to getting familiar with the hammer. Jodi has created her world from a young age.""",6,"lanky-design.html")
detail("auckland-design-week.html","Auckland Design Week.","""After seeing a call out to for designers to create inspired by the nostalgia of the classic NZ dairy, Jodi was eager to put her hat in the ring. This spoke to Jodi as an opportunity to work to another's brief and participate in Auckland Design Week.

Jodi was selected for her idea inspired by the connection that drinks create between people. Coined a ' Golden Connection', Jodi recreated the familiarity of Golden Circle drinks with a lanky twist. The can's shapes were designed to be stored. She experimented with various ways of 'splitting a drink'. This became part of collaborative collection of young designers work exhibited in the showcase.

This opportunity celebrated Jodi the joy of storytelling through her work. She's eager to continue creating with little moments like sharing a drink in her mind.""",4,"lanky-design.html")
detail("look-its-lanky.html","Look it's Lanky.","""As her first exhibit after graduating Jodi was eager to tell everyone ' Look it's Lanky!'

She created a collection of buttons and wee vases that she felt expressed the joy she has in the bright parts of our world. The display was for sale at the Department of Curiosities in Napier and encouraged others to add a little Lanky to their lives.

The love for her buttons showed Jodi that it's often the things as simple as a button that bring immense joy. She continues to look for other things that she can create that ignite creativity in others.""",4,"lanky-design.html")
detail("lanky-kitchen.html","The Lanky Kitchen.","""After designing a rice specific spoon Jodi was eager to turn her love for cooking into a life sized papier mache creation.

From paper towels to a clock, Jodi's kitchen had it all. This was displayed at the EIT design showcase. Created from paper mache, Jodi became very familiar with the flexibility of the medium to translate many items.

This experience sparked an interest in life sized creations for Jodi. She sees the joy in inviting others to her world and sees paper as a fun medium to do so.""",4,"lanky-design.html")
