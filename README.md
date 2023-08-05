# assignTags
assignTags efficiently assigns tags to an entity according to the entity's category and subcategory labels.

### Example

Step 1: create or retrieve legend for tag assignment (tags.xlsx)
|Category|Subcategory|Assignment Conditions|Tags|
|:----|:----|:----|:----|
|ART| |category catch-all|['art']|
|ART|SUPPLIES|sells art supplies|['art supplies', 'paint', 'brush', 'sketch', 'draw', 'color', 'canvas', 'fabric']|
|ART|GALLERY|is an art gallery|['gallery', 'art gallery', 'photography']|
|BOOKS| |category catch-all|['book', 'chapters', 'indigo', 'coles', 'bookstore', 'library']|
|BOOKS|COMICS|is a comic shop|['comic', 'collectable']|
|BOOKS|USED|is a used book store|['used books', 'used bookstore']|
|BUTCHER| |category catch-all|['butcher', 'meat', 'steak', 'sausage', 'grass fed', 'beef']|
|CAFE| |category catch-all|['cafe', 'coffee']|
|CAFE|COFFEE|is a coffee shop|['coffee roaster', 'coffee beans', 'espresso', 'cappiccino', 'latte', 'americano']|
|CAFE|TEA|is a tea shop|['tea']|
|CAFE|BUBBLE_TEA|is a bubble tea shop|['bubble tea', 'boba']|
|FAST_FOOD| |catch-all|['fast food', 'food', 'sandwich', 'lunch', 'drive thru']|
|FAST_FOOD|CLASSIC|sells classic American fast food|['burger', 'fries', 'hot dog', 'chicken nuggets', 'milk shake']|
|FAST_FOOD|PIZZA|is a pizza shop|['pizza', 'slice']|
|FAST_FOOD|HEALTHY|sells health fast food|['salad', 'bowl', 'poke', 'healthy food']|
|GAS_STATION| |catch-all|['gas station', 'gas', 'convenience store', 'cigarettes', 'snacks', 'drinks']|
|TRAVEL| |catch-all|['travel', 'tour', 'sightseeing', 'landmarks', 'vacation']|
|YOGA| |catch-all|['yoga', 'yoga mat', 'hot yoga', 'fitness']|


Step 2: create or retrieve table containing merchant data (merchants.xlsx)
|Brand_Name|Category|Subcategories|Existing_Tags|
|:----|:----|:----|:----|
|Art Gallery of Ontario|ART|GALLERY|["AGO", "Art Gallery of Ontario", "Gallery", "Art"]|
|Jane's Art Supplies|ART|SUPPLIES|["art supplier", "paint"]|
|Second Hand Comics|BOOKS|COMICS, USED|["Marvel", "comics"]|
|The Blue Butcher|BUTCHER| |["butcher", "meat"]|
|Green Tea House|CAFE|TEA, BUBBLE_TEA|["Green Tea House"]|
|Black Coffee Roasters|CAFE|COFFEE|["coffee", "pastries"]|
|Bubba's Burgers|FAST_FOOD|CLASSIC|[]|
|Pizza Pizza|FAST_FOOD|PIZZA|["pizza", "wings", "delivery"]|
|The Poke Bowl|FAST_FOOD|HEALTHY|[]|
|Petro Canada|GAS_STATION| |[]|
|NYC Sightseeing Tours|TRAVEL| |["Tourism"]|
|House of Yoga|YOGA| |["yoga"]|


Step 3: run assignTags.py to assign the category tages you created in step 1 to the merchant table in step 2 (assigned tags.csv)
|Brand_Name|Category|Subcategories|Existing_Tags|Tags|
|:----|:----|:----|:----|:----|
|Art Gallery of Ontario|ART|['GALLERY']|['AGO', 'Art Gallery of Ontario', 'Gallery', 'Art']|['ago', 'art', 'gallery', 'art gallery', 'art gallery of ontario', 'photography']|
|Jane's Art Supplies|ART|['SUPPLIES']|['art supplier', 'paint']|['fabric', 'paint', 'sketch', 'brush', 'art supplies', 'color', 'art', 'art supplier', 'canvas', 'draw']|
|Second Hand Comics|BOOKS|['COMICS', 'USED']|['Marvel', 'comics']|['book', 'marvel', 'library', 'comics', 'used books', 'indigo', 'comic', 'collectable', 'used bookstore', 'bookstore', 'chapters', 'coles']|
|The Blue Butcher|BUTCHER| |['butcher', 'meat']|['beef', 'steak', 'butcher', 'sausage', 'meat', 'grass fed']|
|Green Tea House|CAFE|['TEA', 'BUBBLE_TEA']|['Green Tea House']|['cafe', 'coffee', 'green tea house', 'bubble tea', 'tea', 'boba']|
|Black Coffee Roasters|CAFE|['COFFEE']|['coffee', 'pastries']|['cafe', 'cappiccino', 'americano', 'latte', 'coffee roaster', 'pastries', 'coffee', 'espresso', 'coffee beans']|
|Bubba's Burgers|FAST_FOOD|['CLASSIC']|[]|['sandwich', 'hot dog', 'chicken nuggets', 'milk shake', 'food', 'fries', 'lunch', 'burger', 'fast food', 'drive thru']|
|Pizza Pizza|FAST_FOOD|['PIZZA']|['pizza', 'wings', 'delivery']|['sandwich', 'slice', 'food', 'pizza', 'wings', 'delivery', 'lunch', 'fast food', 'drive thru']|
|The Poke Bowl|FAST_FOOD|['HEALTHY']|[]|['sandwich', 'healthy food', 'salad', 'poke', 'food', 'bowl', 'lunch', 'fast food', 'drive thru']|
|Petro Canada|GAS_STATION| |[]|['cigarettes', 'gas', 'drinks', 'convenience store', 'gas station', 'snacks']|
|NYC Sightseeing Tours|TRAVEL| |['Tourism']|['travel', 'vacation', 'tourism', 'tour', 'sightseeing', 'landmarks']|
|House of Yoga|YOGA| |['yoga']|['yoga mat', 'hot yoga', 'fitness', 'yoga']|
