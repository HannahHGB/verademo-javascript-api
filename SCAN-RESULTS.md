# npm audit report

ansi-regex  4.0.0 - 4.1.0
Severity: high
Inefficient Regular Expression Complexity in chalk/ansi-regex - https://github.com/advisories/GHSA-93q8-gq69-wqmw
fix available via `npm audit fix`
node_modules/cliui/node_modules/ansi-regex
node_modules/yargs/node_modules/ansi-regex

body-parser  <=1.20.3 || 2.0.0-beta.1 - 2.0.2
Severity: high
body-parser vulnerable to denial of service when url encoding is enabled - https://github.com/advisories/GHSA-qwcr-r2fm-qrc7
Depends on vulnerable versions of qs
fix available via `npm audit fix`
node_modules/body-parser
  express  <=4.21.2 || 5.0.0-alpha.1 - 5.0.1
  Depends on vulnerable versions of body-parser
  Depends on vulnerable versions of cookie
  Depends on vulnerable versions of path-to-regexp
  Depends on vulnerable versions of qs
  Depends on vulnerable versions of send
  Depends on vulnerable versions of serve-static
  node_modules/express

brace-expansion  <=1.1.12
Severity: moderate
brace-expansion Regular Expression Denial of Service vulnerability - https://github.com/advisories/GHSA-v6h2-p8h4-qcjw
brace-expansion: Zero-step sequence causes process hang and memory exhaustion - https://github.com/advisories/GHSA-f886-m6hf-6m8v
fix available via `npm audit fix`
node_modules/brace-expansion

braces  <3.0.3
Severity: high
Uncontrolled resource consumption in braces - https://github.com/advisories/GHSA-grv7-fg5c-xmjg
fix available via `npm audit fix`
node_modules/braces

cookie  <0.7.0
cookie accepts cookie name, path, and domain with out of bounds characters - https://github.com/advisories/GHSA-pxg6-pf52-xh8x
fix available via `npm audit fix`
node_modules/cookie

curling  <=1.0.0
Severity: high
OS Command Injection in curling - https://github.com/advisories/GHSA-xmxh-g7wj-8m4m
fix available via `npm audit fix --force`
Will install curling@1.1.0, which is a breaking change
node_modules/curling

diff  4.0.0 - 4.0.3
jsdiff has a Denial of Service vulnerability in parsePatch and applyPatch - https://github.com/advisories/GHSA-73rr-hh4g-fpgx
fix available via `npm audit fix`
node_modules/diff

djv  <2.1.4
Severity: critical
Arbitrary code execution in djv - https://github.com/advisories/GHSA-4hv7-3q38-97m8
fix available via `npm audit fix`
node_modules/djv


handlebars  4.0.0 - 4.7.8
Severity: critical
Handlebars.js has JavaScript Injection via AST Type Confusion by tampering @partial-block - https://github.com/advisories/GHSA-3mfm-83xf-c92r
Handlebars.js has JavaScript Injection via AST Type Confusion - https://github.com/advisories/GHSA-2w6w-674q-4c4q
Handlebars.js has Prototype Pollution Leading to XSS through Partial Template Injection - https://github.com/advisories/GHSA-2qvq-rjwj-gvw9
Handlebars.js has a Prototype Method Access Control Gap via Missing __lookupSetter__ Blocklist Entry - https://github.com/advisories/GHSA-7rx3-28cr-v5wh
Handlebars.js has a Property Access Validation Bypass in container.lookup - https://github.com/advisories/GHSA-442j-39wm-28r2
Handlebars.js has JavaScript Injection via AST Type Confusion when passing an object as dynamic partial - https://github.com/advisories/GHSA-xhpv-hc6g-r9c6
Handlebars.js has Denial of Service via Malformed Decorator Syntax in Template Compilation - https://github.com/advisories/GHSA-9cx6-37pm-9jff
Handlebars.js has JavaScript Injection in CLI Precompiler via Unescaped Names and Options - https://github.com/advisories/GHSA-xjpj-3mr7-gcpf
fix available via `npm audit fix`
node_modules/handlebars

js-yaml  <=3.14.2 || 4.0.0 - 4.1.1
Severity: moderate
js-yaml has prototype pollution in merge (<<) - https://github.com/advisories/GHSA-mh29-5h37-fv8m
js-yaml has prototype pollution in merge (<<) - https://github.com/advisories/GHSA-mh29-5h37-fv8m
JS-YAML: Quadratic-complexity DoS in merge key handling via repeated aliases - https://github.com/advisories/GHSA-h67p-54hq-rp68
JS-YAML: Quadratic-complexity DoS in merge key handling via repeated aliases - https://github.com/advisories/GHSA-h67p-54hq-rp68
fix available via `npm audit fix --force`
Will install swagger-jsdoc@6.3.0, which is a breaking change
node_modules/js-yaml
node_modules/swagger-jsdoc/node_modules/js-yaml
  swagger-jsdoc  3.0.0 - 5.0.1
  Depends on vulnerable versions of js-yaml
  node_modules/swagger-jsdoc

lodash  <=4.17.23
Severity: high
Command Injection in lodash - https://github.com/advisories/GHSA-35jh-r3h4-6jhm
Prototype Pollution in lodash - https://github.com/advisories/GHSA-p6mc-m468-83gw
Regular Expression Denial of Service (ReDoS) in lodash - https://github.com/advisories/GHSA-29mw-wpgm-hmr9
lodash vulnerable to Code Injection via `_.template` imports key names - https://github.com/advisories/GHSA-r5fr-rjxr-66jc
lodash vulnerable to Prototype Pollution via array path bypass in `_.unset` and `_.omit` - https://github.com/advisories/GHSA-f23m-r3pf-42rh
Lodash has Prototype Pollution Vulnerability in `_.unset` and `_.omit` functions - https://github.com/advisories/GHSA-xxjr-mmjv-4gpg
fix available via `npm audit fix`
node_modules/concurrently/node_modules/lodash
node_modules/lodash

minimatch  <=3.1.3
Severity: high
minimatch has a ReDoS via repeated wildcards with non-matching literal in pattern - https://github.com/advisories/GHSA-3ppc-4f35-3m26
minimatch has ReDoS: matchOne() combinatorial backtracking via multiple non-adjacent GLOBSTAR segments - https://github.com/advisories/GHSA-7r86-cg39-jmmj
minimatch ReDoS: nested *() extglobs generate catastrophically backtracking regular expressions - https://github.com/advisories/GHSA-23c5-xmqv-rm74
fix available via `npm audit fix`
node_modules/minimatch

minimist  1.0.0 - 1.2.5
Severity: critical
Prototype Pollution in minimist - https://github.com/advisories/GHSA-xvch-5gv4-984h
fix available via `npm audit fix`
node_modules/minimist

on-headers  <1.1.0
on-headers is vulnerable to http response header manipulation - https://github.com/advisories/GHSA-76c9-3jph-rj3q
fix available via `npm audit fix`
node_modules/on-headers
  morgan  1.6.0 - 1.10.0
  Depends on vulnerable versions of on-headers
  node_modules/morgan

path-to-regexp  <=0.1.12
Severity: high
path-to-regexp outputs backtracking regular expressions - https://github.com/advisories/GHSA-9wv6-86v2-598j
path-to-regexp contains a ReDoS - https://github.com/advisories/GHSA-rhx6-c78j-4q9w
path-to-regexp vulnerable to Regular Expression Denial of Service via multiple route parameters - https://github.com/advisories/GHSA-37ch-88jc-xwx2
fix available via `npm audit fix`
node_modules/path-to-regexp

picomatch  <=2.3.1
Severity: high
Picomatch: Method Injection in POSIX Character Classes causes incorrect Glob Matching - https://github.com/advisories/GHSA-3v7f-55p6-f55p
Picomatch has a ReDoS vulnerability via extglob quantifiers - https://github.com/advisories/GHSA-c2c7-rcm5-vvqj
fix available via `npm audit fix`
node_modules/picomatch

qs  <=6.14.1
Severity: moderate
qs's arrayLimit bypass in comma parsing allows denial of service - https://github.com/advisories/GHSA-w7fw-mjwx-w883
qs's arrayLimit bypass in its bracket notation allows DoS via memory exhaustion - https://github.com/advisories/GHSA-6rw7-vpxm-498p
fix available via `npm audit fix`
node_modules/qs

send  <0.19.0
send vulnerable to template injection that can lead to XSS - https://github.com/advisories/GHSA-m6fv-jmcg-4jfg
fix available via `npm audit fix`
node_modules/send
  serve-static  <=1.16.0
  Depends on vulnerable versions of send
  node_modules/serve-static


url-parse  <=1.5.8
Severity: critical
Authorization Bypass Through User-Controlled Key in url-parse - https://github.com/advisories/GHSA-hgjh-723h-mx2j
url-parse incorrectly parses hostname / protocol due to unstripped leading control characters. - https://github.com/advisories/GHSA-jf5r-8hm2-f872
url-parse Incorrectly parses URLs that include an '@' - https://github.com/advisories/GHSA-8v38-pw62-9cw2
Authorization bypass in url-parse - https://github.com/advisories/GHSA-rqff-837h-mm52
fix available via `npm audit fix`
node_modules/url-parse

validator  <=13.15.20
Severity: high
validator.js has a URL validation bypass vulnerability in its isURL function - https://github.com/advisories/GHSA-9965-vmph-33xx
Validator is Vulnerable to Incomplete Filtering of One or More Instances of Special Elements - https://github.com/advisories/GHSA-vghf-hv5q-vc2g
fix available via `npm audit fix`
node_modules/validator

vm2  <=3.11.3
Severity: critical
vm2 vulnerable to Arbitrary Code Execution - https://github.com/advisories/GHSA-4w2j-2rg4-5mjw
vm2 vulnerable to Sandbox Escape resulting in Remote Code Execution on host - https://github.com/advisories/GHSA-mrgp-mrhc-5jrq
Sandbox bypass in vm2 - https://github.com/advisories/GHSA-6pw2-5hjv-9pf7
vm2 vulnerable to sandbox escape - https://github.com/advisories/GHSA-7jxr-cg7f-gpgv
vm2 Sandbox Escape vulnerability - https://github.com/advisories/GHSA-ch3r-j5x3-6q2m
vm2 Sandbox Escape vulnerability - https://github.com/advisories/GHSA-whpj-8f3w-67p5
vm2 vulnerable to Inspect Manipulation - https://github.com/advisories/GHSA-p5gc-c584-jj6v
vm2 Sandbox Escape vulnerability - https://github.com/advisories/GHSA-xj72-wvfv-8985
vm2 Sandbox Escape vulnerability - https://github.com/advisories/GHSA-g644-9gfx-q4q4
vm2 Sandbox Escape vulnerability - https://github.com/advisories/GHSA-cchq-frgv-rjh5
vm2 has a Sandbox Escape - https://github.com/advisories/GHSA-99p7-6v5w-7xg8
VM2 Has a Sandbox Escape Issue via SuppressedError - https://github.com/advisories/GHSA-55hx-c926-fr95
VM2 Has Sandbox Breakout Through Inspect Function - https://github.com/advisories/GHSA-v37h-5mfm-c47c
VM2 Has Sandbox Breakout Through Promise Species - https://github.com/advisories/GHSA-qvjj-29qf-hp7p
VM2 Sandbox Breakout Through __lookupGetter__ - https://github.com/advisories/GHSA-grj5-jjm8-h35p
vm2 has access to `VM2_INTERNAL_STATE_DO_NOT_USE_OR_PROGRAM_WILL_FAIL` - https://github.com/advisories/GHSA-2cm2-m3w5-gp2f
vm2 has Sandbox Breakout Through Null Proto Exception - https://github.com/advisories/GHSA-9vg3-4rfj-wgcm
vm2 has sandbox breakout via `neutralizeArraySpeciesBatch` - https://github.com/advisories/GHSA-9qj6-qjgg-37qq
vm2 NodeVM `nesting: true` bypasses `require: false` allowing sandbox escape and arbitrary OS command execution - https://github.com/advisories/GHSA-8hg8-63c5-gwmx
vm2's Transformer Fast-Path Bypass Exposes Internal State Variable - https://github.com/advisories/GHSA-wp5r-2gw5-m7q7
vm2 is Vulnerable to Host File Path Disclosure via Stack Trace Information Leak - https://github.com/advisories/GHSA-v27g-jcqj-v8rw
vm2 Host Promise Resolution Preserves Object Identity Across Sandbox Boundary - https://github.com/advisories/GHSA-mpf8-4hx2-7cjg
vm2 Sandbox Access to Host Buffer.alloc Allows timeout Bypass Resulting in Memory Exhaustion - https://github.com/advisories/GHSA-6785-pvv7-mvg7
vm2 has a Sandbox Escape via Promise Constructor Unhandled Rejection (Process Crash DoS) - https://github.com/advisories/GHSA-hw58-p9xv-2mjh
vm2 Access to Host Object Enables Sandbox Escape - https://github.com/advisories/GHSA-47x8-96vw-5wg6
vm2 has a Sandbox Escape Vulnerability - https://github.com/advisories/GHSA-qcp4-v2jj-fjx8
vm2 Has a Sandbox Breakout Using Async Generator - https://github.com/advisories/GHSA-248r-7h7q-cr24
vm2 setup-sandbox.js violates Defense Invariant #11 in stack-trace formatter - https://github.com/advisories/GHSA-q3fm-4wcw-g57x
VM2 Has a WASM Sandbox Escape - https://github.com/advisories/GHSA-ffh4-j6h5-pg66
NodeVM observability builtins leak host process and HTTP request data - https://github.com/advisories/GHSA-9g8x-92q2-p28f
NodeVM network builtin exclusions bypass via internal _http_client and _http_server - https://github.com/advisories/GHSA-r9pm-gxmw-wv6p
vm2's Bridge Proxy set trap ignores receiver parameter, enabling host object property injection via prototype chain - https://github.com/advisories/GHSA-c4cf-2hgv-2qv6
vm2 has a sandbox escape via unblocked cross-realm Symbol.for keys + missing bridge write-trap symbol checks - https://github.com/advisories/GHSA-m5q2-4fm3-vfqp
NodeVM builtin denylist bypass via process and inspector/promises allows host code execution - https://github.com/advisories/GHSA-rp36-8xq3-r6c4
vm2 sandbox escape via JSPI-backed Promise `.finally()` species bypass - https://github.com/advisories/GHSA-6j2x-vhqr-qr7q
vm2 has a CVE-2023-37903 patch bypass: nesting:true without explicit require still allows full RCE - https://github.com/advisories/GHSA-m4wx-m65x-ghrr
vm2 is Vulnerable to Sandbox Breakout Through Promise Species - https://github.com/advisories/GHSA-76w7-j9cq-rx2j
vm2 has a Sandbox Escape issue - https://github.com/advisories/GHSA-v6mx-mf47-r5wg
fix available via `npm audit fix`
node_modules/vm2

25 vulnerabilities (6 low, 4 moderate, 10 high, 5 critical)

To address issues that do not require attention, run:
  npm audit fix

To address all issues (including breaking changes), run:
  npm audit fix --force
