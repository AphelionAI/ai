// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
const vscode = require('vscode');

// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {


	// Use the console to output diagnostic information (console.log) and errors (console.error)
	// This line of code will only be executed once when your extension is activated
	console.log('Aphelion autocomplete now active');


	let disposable = vscode.commands.registerCommand('aphelion.helloWorld', function () {
		// The code you place here will be executed every time your command is executed

		// Display a message box to the user
		vscode.window.showInformationMessage('Hello World from aphelion!');
	});

	const provider = {
		provideInlineCompletionItems: async (document, position, context, token) => {
			const line = document.lineAt(position.line);
			console.log("420")
			// Here we need to call the python code for generating stuff
			if (line.text.startsWith('if')) {
				console.log("421")
				let range = line.range;
				if (line.text.indexOf(";") !== -1) {
					console.log("422")
					range = new vscode.Range(range.start, range.end.with(undefined, line.text.indexOf(";") + 1));
				}
				console.log("423")
				return [{ text: 'if (hello) {\n};', insertText: "if (hello)", range }];
			}
		}
	};
	vscode.languages.registerInlineCompletionItemProvider({ pattern: '**' }, provider);

	context.subscriptions.push(disposable);
}

// This method is called when your extension is deactivated
function deactivate() { }

module.exports = {
	activate,
	deactivate
}
