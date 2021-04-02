from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

# accepts post
# post route ==> has a body
@app.route('/id', methods=['POST'])
def get_id():
    # import pdb; pdb.set_trace()  # BREAKPOINT AND CHECK VARIABLES ETC IN CMDPROMPT
    
    print(request.json, "XXXXX")
    translated = BN_translator(request.json) # translated is an instance of the class NodeData
    reversal = find_reversal(translated.relevant_inputs) # reversal is the determined optimal reversal
    result = [updated_prob, network] = edge_switch(reversal) # result is a block of updated probs, new network, etc
    decoded = BN_decoder(result) # decoded is a json dict to return to frontend

    return decoded

app.run(debug = True)
