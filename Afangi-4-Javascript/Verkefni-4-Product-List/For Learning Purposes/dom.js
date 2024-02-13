// DOM selectors skila HTMLCollection eða NodeList. skoðum muninn.

	// Við viljum fá vísun á og halda utan um öll innri div element í container.
	
		// prófum querySelectorAll 
		let nodeListDivs = document.querySelectorAll('.divy');	
		console.log(typeof(nodeListDivs));							//=> Object
		console.log(Array.isArray(nodeListDivs)); 					//=> false, childDivs er ekki array
		console.log(nodeListDivs.constructor.name); 				//=> static NodeList
		console.log(nodeListDivs.length); 							//=> 4

		// Prófum getElementByClassName 
		let htmlCollectionDivs = document.getElementsByClassName('divy')
		console.log(typeof(htmlCollectionDivs));					//=> Object
		console.log(Array.isArray(htmlCollectionDivs));				//=> false, ekki array
		console.log(htmlCollectionDivs.constructor.name);			//=> HTMLCollection
		console.log(htmlCollectionDivs.length); 					//=> 4

		// Búum til og bætum við nýtt div í html
		var newDiv = document.createElement('div');
		newDiv.className = 'divy';
		let parentDiv = document.getElementById('container');	
		parentDiv.appendChild(newDiv);

		// Skoðum núna hvað hefur breyst. 
		console.log(nodeListDivs.length);							//=> 4   uppfærist ekki, static NodeList
		console.log(htmlCollectionDivs.length); 					//=> 5 	 uppfært,live HTMLCollection
		
		/*
			live: 		Breytingar í DOM er uppfært sjálfvirkt og aðgengilegt í safni (e. collection).
			static:		Breytingar í DOM hefur ekki áhrif á innihald í safni.
			
			- Öll HTMLCollections eru live
			- NodeList objects eru static eða live

			DOM Selectors aðferðir:

				document.getElementById()					// Element 
				document.querySelector()					// first Element returned
				
				document.getElementsByTagName()				// HTMLCollection
				document.getElementsByClassName()			// HTMLCollection

				document.getElementsByName()				// live NodeList
				document.querySelectorAll()					// static NodeList
			
			Node interface:
			
				Node.firstChild;							// fist Node
				Node.lastChild;								// last Node
				Node.nextSibling;							// next Node
				Node.previousSibling;						// previous Node
				Node.parentNode;							// parent of Node
				Node.parentElement;							// Element of node
				Node.childNodes;							// live NodeList

			KóðaSkýringarMyndband: 
			Sýnir allar DOM Selector aðferðir og muninn á Nodelist og HTMLCollection
			https://www.youtube.com/watch?v=mXOGpcm19J8

		HTMLCollection vs NodeList:

			- Bæði NodeList og HTMLCollection eru safn of nodes. 
			- NodeList getur innihaldið öll nodes (element, attribute, text, document, comment osfrv). 
			- HTMLCollection inniheldur aðeins HTML elements (tags)
			- Ef þú you vilt ávallt ítra yfir uppfært DOM þá notar þú Live NodeList eða HTMLCollection. 
			- Nodelist og HTMLCollection hafa mismunandi aðferðir sem hægt er að nota (sjá aðerðir og eigindi nánar í linkum neðar í skrá)
			  Við getum td. ekki notað t.d. push/pop/splice/filter og fleiri array aðferðir þar sem þetta eru ekki fylki. 
			  Það er þó mögulegt að breyta NodeList og HTMLCollection í Array t.d. með Array.from() eða spread operator 
		

			-- HTMLCollection:

					let htmlCollectionDivs = document.getElementsByClassName('divy')  	// DOM selector sem skilar HTMLCollection
					console.log(htmlCollectionDivs.item(0));							// item() aðferð sem HTMLCollection á til að velja node 

			-- NodeList:
					
					let parent = document.getElementById('container');
					let child_nodes = parent.childNodes;								// Node.childNodes skilar a live NodeList
					console.log(child_nodes.constructor.name); 							// NodeList
					console.log(child_nodes.length); 									// 4, ath. mundu eftir white space


		DOM interfaces
		https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model
				
				Node
					https://developer.mozilla.org/en-US/docs/Web/API/Node
					
				NodeList
					https://developer.mozilla.org/en-US/docs/Web/API/NodeList

				Element
					https://developer.mozilla.org/en-US/docs/Web/API/Element
					
				HTMLCollection 
					https://developer.mozilla.org/en-US/docs/Web/API/HTMLCollection

				DOM interfaces
					https://developer.mozilla.org/en-US/docs/Web/API/DOMTokenList

		*/