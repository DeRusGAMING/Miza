(this.webpackJsonpmizaweb2=this.webpackJsonpmizaweb2||[]).push([[378,190],{271:function(e,n){e.exports=function(e){var n={className:"string",contains:[e.BACKSLASH_ESCAPE],variants:[e.inherit(e.APOS_STRING_MODE,{illegal:null}),e.inherit(e.QUOTE_STRING_MODE,{illegal:null})]},i=e.UNDERSCORE_TITLE_MODE,s={variants:[e.BINARY_NUMBER_MODE,e.C_NUMBER_MODE]},a="namespace class interface use extends function return abstract final public protected private static deprecated throw try catch Exception echo empty isset instanceof unset let var new const self require if else elseif switch case default do while loop for continue break likely unlikely __LINE__ __FILE__ __DIR__ __FUNCTION__ __CLASS__ __TRAIT__ __METHOD__ __NAMESPACE__ array boolean float double integer object resource string char long unsigned bool int uint ulong uchar true false null undefined";return{name:"Zephir",aliases:["zep"],keywords:a,contains:[e.C_LINE_COMMENT_MODE,e.COMMENT(/\/\*/,/\*\//,{contains:[{className:"doctag",begin:/@[A-Za-z]+/}]}),{className:"string",begin:/<<<['"]?\w+['"]?$/,end:/^\w+;/,contains:[e.BACKSLASH_ESCAPE]},{begin:/(::|->)+[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*/},{className:"function",beginKeywords:"function fn",end:/[;{]/,excludeEnd:!0,illegal:/\$|\[|%/,contains:[i,{className:"params",begin:/\(/,end:/\)/,keywords:a,contains:["self",e.C_BLOCK_COMMENT_MODE,n,s]}]},{className:"class",beginKeywords:"class interface",end:/\{/,excludeEnd:!0,illegal:/[:($"]/,contains:[{beginKeywords:"extends implements"},i]},{beginKeywords:"namespace",end:/;/,illegal:/[.']/,contains:[i]},{beginKeywords:"use",end:/;/,contains:[i]},{begin:/=>/},n,s]}}},766:function(e,n,i){!function e(){e.warned||(e.warned=!0,console.log('Deprecation (warning): Using file extension in specifier is deprecated, use "highlight.js/lib/languages/zephir" instead of "highlight.js/lib/languages/zephir.js"'))}(),e.exports=i(271)}}]);
//# sourceMappingURL=378.32533263.chunk.js.map