// 2.2 

const add = function(a, b) {
    return a + b;
  }

sum = add(1,2);
console.log(sum);

const add2 = (a,b) => a + b;

sum = add2(1,2);
console.log(sum);

// 2.3
let numbers = [1, 2, 3, 4, 5];

let oddNumbers = [];

for (let i = 0; i<numbers.length; i++) {
    if (numbers[i]%2 != 0){
        oddNumbers.push(numbers[i]);
    }
}


console.log(oddNumbers);  // [1,3,5]

oddNumbers = [];

numbers.map(x => {
    if(x%2!=0) {
        oddNumbers.push(x);
    }  
}
)
console.log(oddNumbers);  // [1,3,5]

// 2.4
let personuUplysingar = {
    nafn : "Þórður Ingi",
    faedingarAr : 2003,
    email : ["thorduringis@gmail.com","toto@gmail.com","doddi@gmail.com"],
    nafnAldur : function() {return `Nafn: ${this.nafn} Aldur: ${2021 - this.faedingarAr}`}
}

console.log(personuUplysingar.nafnAldur());
//2.5
let family = {
    "parents": 
        {
        "fathers": [{"name":"Jakob"},{"name":"Nonni"}],
        "mothers":[{"name":"Rakel"},{"name":"Sara"}]
        }
};

console.log(family.parents.fathers[1].name);


const result = {
    success: ["max-length", "no-amd", "prefer-arrow-functions"],
    failure: ["no-var", "var-on-top", "linebreak"],
    skipped: ["no-extra-semi", "no-dup-keys"]
  };
  function makeList(arr) {

    const failureItems = arr.map(x => `<li class="text-warning">${x}</li>'`);

  
    return failureItems;
  }
  
  const failuresList = makeList(result.failure);
  
  console.log(failuresList);

// 2.6

class User {
    constructor(nafn,netfang) {
        this.nafn = nafn;
        this.netfang = netfang;
    }

    get nafnget() {
        return this.nafn;
    }

    set nafnset(nyttnafn){
        this.nafn = nyttnafn;
    }
}

madur = new User("NonniJon","Nonni@gmail.com");

for (i in madur) {
    console.log(madur[i]);
}
// 2.7
class Animal {
    constructor(nafn,speed = 0){
        this.nafn = nafn;
        this.speed = speed;
    }
    run() {
        this.speed += 1;
    }
}

class Rabbit extends Animal {
    constructor(hophaed) {
        this.hophaed = hophaed;
        super(nafn,speed);
    }
    jump(){
        this.hophaed +=1;
    }
}

// 2.8
function Userconstructor(nafn,netfang) {
    this.nafn = nafn;
    this.netfang = netfang;
}
Userconstructor.prototype.getUser = function(){
    return this.nafn;
}


const doddi = new Userconstructor("Thordur","thorduringis@gmail.com");
console.log(doddi.nafn,doddi.netfang,doddi.getUser());
// 2.9

let cart=[
    {name:"Biscuits", type:"regular", category:"food", price: 2.0},
    {name:"Monitor", type:"prime", category:"tech", price: 119.99},
    {name:"Mouse", type:"prime", category:"tech", price: 25.50},
    {name:"dress", type:"regular", category:"clothes", price: 49.90},
  ]

const afslatt = (kodi) => {
    let uppfaerdKarfa = [];
    for (let i = 0; i<cart.length;i++) {
        if (cart[i].category == "tech") {
            let techVara = cart[i];
            techVara.price = techVara.price*0.8; 
            uppfaerdKarfa.push(techVara);
        }
    }
    return uppfaerdKarfa;
} 
let a = prompt("Sláðu inn afsláttar kóða","Kóði")
console.log(afslatt(a));

