
def get_all_books():
    """Get List of all books"""
    response = requests.get('https://simple-books-api.glitch.me/books')
    res_json = response.json()
    res_str = json.dumps(res_json)
    return res_str



def get_book_id(name):
    """Get Book Id from name"""
    response = requests.get('https://simple-books-api.glitch.me/books')
    res_json = response.json()

    for book in res_json:
        if book['name'] == name:
            return book['id']


def getprice(name):
    """Get Book price by name"""
    bookid = get_book_id(name)
    response = requests.get(f"https://simple-books-api.glitch.me/books/{bookid}")
    res_json = response.json()
    get_Price = res_json['price']
    res_str = json.dumps(get_Price)
    return res_str


def get_single_book(name):
    """Get Single Book Details by name"""
    bookid = get_book_id(name)
    response = requests.get(f"https://simple-books-api.glitch.me/books/{bookid}")
    res_json = response.json()
    res_str = json.dumps(res_json)
    return res_str


def connector(key, prompt):
    """
    Get Api key and prompt
    """
    if not key or not prompt:
        raise ValueError("Error: OpenAi API Key and Your Query are also required")
    
    client = OpenAI(api_key=key)
    
    def run_conversation(main_request: str) -> str:
        """
        Step 1: send the conversation and available functions to the model
        """
        messages = [{"role": "user", "content": main_request}]  # user's message
        tools = [
            {
                "type": "function",
                "function": {
                    "name": "get_all_books",
                    "description": "Get the list of books",
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "getprice",
                    "description": "Get the price by its name",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string",
                                "description": "name of book, e.g. The Russian",
                            }},
                        "required": ["name"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "get_single_book",
                    "description": "Get the Whole Detail of by its name",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string",
                                "description": "name of book, e.g. The Russian",
                            }},
                        "required": ["name"],
                    },
                },
            },
            
        ]

        # First Request
        response: ChatCompletion = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=messages,
            tools=tools,
            tool_choice="auto",  # auto is default, but we'll be explicit
        )
        response_message: ChatCompletionMessage = response.choices[0].message
        print("* First Response: ", dict(response_message))

        tool_calls = response_message.tool_calls
        print("* First Reponse Tool Calls: ", list(tool_calls))

        # Step 2: check if the model wanted to call a function
        if tool_calls:
            # Step 3: call the function
            # Note: the JSON response may not always be valid; be sure to handle errors
            available_functions = {
                "get_all_books": get_all_books,
                "getprice":getprice,
                "get_single_book":get_single_book,
                
            }  # only one function in this example, but you can have multiple

            messages.append(response_message)  # extend conversation with assistant's reply

            # Step 4: send the info for each function call and function response to the model
            for tool_call in tool_calls:
                function_name = tool_call.function.name
                function_to_call = available_functions[function_name]
                function_args = json.loads(tool_call.function.arguments)
                if function_to_call.__name__ == "get_all_books":
                    function_response = function_to_call()
                    messages.append({
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": function_name,
                        "content": function_response,
                    })  # extend conversation with function response
                else:
                    function_response = function_to_call(
                        name=function_args.get("name"),  # put location from prompt into location
                    )
                    messages.append(
                        {
                            "tool_call_id": tool_call.id,
                            "role": "tool",
                            "name": function_name,
                            "content": function_response,
                        }
                    )  # extend conversation with function response

            print("* Second Request Messages: ", list(messages))
            second_response: ChatCompletion = client.chat.completions.create(
                model="gpt-3.5-turbo-1106",
                messages=messages,
            )  # get a new response from the model where it can see the function response
            print("* Second Response: ", dict(second_response))
            return second_response.choices[0].message.content
        
    chat_result = run_conversation(prompt)
    return chat_result
