(this.webpackJsonpmizaweb2=this.webpackJsonpmizaweb2||[]).push([[340,152],{233:function(e,n){function t(e){return e?"string"===typeof e?e:e.source:null}function i(){for(var e=arguments.length,n=new Array(e),i=0;i<e;i++)n[i]=arguments[i];var a=n.map((function(e){return t(e)})).join("");return a}e.exports=function(e){var n,t={className:"title.function.invoke",relevance:0,begin:i(/\b/,/(?!let\b)/,e.IDENT_RE,(n=/\s*\(/,i("(?=",n,")")))},a="([ui](8|16|32|64|128|size)|f(32|64))?",s=["drop ","Copy","Send","Sized","Sync","Drop","Fn","FnMut","FnOnce","ToOwned","Clone","Debug","PartialEq","PartialOrd","Eq","Ord","AsRef","AsMut","Into","From","Default","Iterator","Extend","IntoIterator","DoubleEndedIterator","ExactSizeIterator","SliceConcatExt","ToString","assert!","assert_eq!","bitflags!","bytes!","cfg!","col!","concat!","concat_idents!","debug_assert!","debug_assert_eq!","env!","panic!","file!","format!","format_args!","include_bin!","include_str!","line!","local_data_key!","module_path!","option_env!","print!","println!","select!","stringify!","try!","unimplemented!","unreachable!","vec!","write!","writeln!","macro_rules!","assert_ne!","debug_assert_ne!"];return{name:"Rust",aliases:["rs"],keywords:{$pattern:e.IDENT_RE+"!?",type:["i8","i16","i32","i64","i128","isize","u8","u16","u32","u64","u128","usize","f32","f64","str","char","bool","Box","Option","Result","String","Vec"],keyword:["abstract","as","async","await","become","box","break","const","continue","crate","do","dyn","else","enum","extern","false","final","fn","for","if","impl","in","let","loop","macro","match","mod","move","mut","override","priv","pub","ref","return","self","Self","static","struct","super","trait","true","try","type","typeof","unsafe","unsized","use","virtual","where","while","yield"],literal:["true","false","Some","None","Ok","Err"],built_in:s},illegal:"</",contains:[e.C_LINE_COMMENT_MODE,e.COMMENT("/\\*","\\*/",{contains:["self"]}),e.inherit(e.QUOTE_STRING_MODE,{begin:/b?"/,illegal:null}),{className:"string",variants:[{begin:/b?r(#*)"(.|\n)*?"\1(?!#)/},{begin:/b?'\\?(x\w{2}|u\w{4}|U\w{8}|.)'/}]},{className:"symbol",begin:/'[a-zA-Z_][a-zA-Z0-9_]*/},{className:"number",variants:[{begin:"\\b0b([01_]+)"+a},{begin:"\\b0o([0-7_]+)"+a},{begin:"\\b0x([A-Fa-f0-9_]+)"+a},{begin:"\\b(\\d[\\d_]*(\\.[0-9_]+)?([eE][+-]?[0-9_]+)?)"+a}],relevance:0},{begin:[/fn/,/\s+/,e.UNDERSCORE_IDENT_RE],className:{1:"keyword",3:"title.function"}},{className:"meta",begin:"#!?\\[",end:"\\]",contains:[{className:"string",begin:/"/,end:/"/}]},{begin:[/let/,/\s+/,/(?:mut\s+)?/,e.UNDERSCORE_IDENT_RE],className:{1:"keyword",3:"keyword",4:"variable"}},{begin:[/for/,/\s+/,e.UNDERSCORE_IDENT_RE,/\s+/,/in/],className:{1:"keyword",3:"variable",5:"keyword"}},{begin:[/type/,/\s+/,e.UNDERSCORE_IDENT_RE],className:{1:"keyword",3:"title.class"}},{begin:[/(?:trait|enum|struct|union|impl|for)/,/\s+/,e.UNDERSCORE_IDENT_RE],className:{1:"keyword",3:"title.class"}},{begin:e.IDENT_RE+"::",keywords:{keyword:"Self",built_in:s}},{className:"punctuation",begin:"->"},t]}}},727:function(e,n,t){!function e(){e.warned||(e.warned=!0,console.log('Deprecation (warning): Using file extension in specifier is deprecated, use "highlight.js/lib/languages/rust" instead of "highlight.js/lib/languages/rust.js"'))}(),e.exports=t(233)}}]);
//# sourceMappingURL=340.e4412443.chunk.js.map