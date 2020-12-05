source_dir := "notes"
build_html_dir := source_dir + "/_build/html"

# Does not work: --builder linkcheck
links:
   jupyter-book build {{source_dir}} --builder linkcheck

build:
   jupyter-book build {{source_dir}}

show:
   start {{build_html_dir}}/index.html

clean:
   rm -rf {{build_html_dir}}

publish:
   just clean
   just build
   just pages

pages:
   ghp-import -n -p -f {{build_html_dir}}
