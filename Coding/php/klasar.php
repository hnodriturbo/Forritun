 <!-- ----- KLASAR OG OBJECTS ----- -->
<?php
    // bý til klasann
    class book {
        var $title;
        var $author;
        var $pages;

        // Smiður innan í klasanum
        function __construct($aTitle,$aAuthor,$aPages){
            $this->title = $aTitle;
            $this->author = $aAuthor;
            $this->pages = $aPages;
        }
        // Functions inn í klasanum er hægt að nota utan klasans
    }
/*     // bý til nokkrar bækur í klasann book
    $book2 = new book();
    $book2->title = "Something 1";
    $book2->author = "Author 1";
    $book2->pages = 600;

    $book3 = new book();
    $book3->title = "Something 2";
    $book3->author = "Author 2";
    $book3->pages = 200;
  */
    // Þessi notar constructorinn til að búa til $book1
    $book1 = new book("Harry Potter","JK Rowling",400);

    // set bækurnar inn í breytu sem array objects
    $books = array($book1);

    // Dæmi um hvernig er hægt að nálgast upplýsingar úr $books array
    foreach ($books as $book) {
        echo "Title: " . $book->title . "<br>";
        echo "Author: " . $book->author . "<br>";
        echo "Pages: " . $book->pages . "<br>";
    } 
?>

<!-- Annað klasa dæmi með function inn í klasa -->
<?php
    class Student {
        var $name;
        var $major;
        var $einkun;
    
        function __construct($name, $major, $einkun) {
            $this->name = $name;
            $this->major = $major;
            $this->einkun = $einkun;
        }
        function hasHonors() {
            if($this->einkun >= 3.5) {
                return "true";
            } else {
                return "false";
            }
        }
    }

    $student1 = new Student("Jim","Business", 2.8);
    $student2 = new Student("Hreiðar","Tölvur", 10.0);

    echo $student1->hasHonors();
?>
<!-- Annað klasa dæmi með getter og setter -->
<?php

class Movie {
    // Public þýðir að breytan er aðgengileg hvar sem er í kóðanum
    public $title;
    public $rating;

    // Constructor
    function __construct($title, $rating) {
        $this->title = $title;
        $this->rating = $rating;

    
    }
    // Destructor
    function __destruct() {
        // destructor
    }
    
    // Getter
    function getRating() {
        return $this->rating;
    }

    // Setter
    function setRating($newRating) {
        $this->rating = $newRating;
    }
    
    
}

$avengers = new Movie("Avengers", "PG-13");


echo $avengers->rating;
$avengers->setRating(10);
$einkunn = $avengers->getRating();
echo $einkunn
?>

<!-- Klasar og erfðir -->

<?php

    class Chef {
        function makeChicken() {
            echo "The chef makes chicken <br>";
        }
        // hægt að gera fullt af functions meira
        // sá sem erfir þennan klasa getur notað functions úr þessum klasa
    }

    class ItalianChef extends Chef {
        // aðeins þessi klasi hefur aðgang að makePasta
        function makePasta(){
            echo "The chef makes pasta";
        }
    }


    $chef = new Chef();
    $chef->makeChicken();
    // seinni klasinn erfir functions frá hinum klasanum
    $ItalianChef = new Chef();
    $ItalianChef->makeChicken();


?>




<?php

class Fruit {
    public $name; 
    public $color;


    function __construct($name, $color){
        $this->name = $name;
        $this->color = $color;
    }

    public function intro() {
        echo "{$this->name} is a fruit and color is {$this->color}";
    }
}
// skilgreini klasa og hann extendar(erfir) fruit klasa eiginleikana
class Cherry extends fruit {
    public $weight;
    public function __construct($name, $color, $weight) {
        $this->name = $name;
        $this->color = $color;
        $this->weight = $weight;
    }
    
    public function message() {
        echo "is cherry a fruit or a berry?";
    }

    public function intro() {
        echo "{$this->name} is a fruit and color is {$this->color} and the weight is {$this->weight}";
    }


}  
$cherry = new cherry ("cherry","red",20);
echo "<br><br><br>";
$cherry->message();
echo "<br><br><br>";
$cherry->intro(); 
?>