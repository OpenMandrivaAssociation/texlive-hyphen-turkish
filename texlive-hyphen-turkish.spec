%global tl_name hyphen-turkish
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Turkish hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/hyphenation/tkhyph.tex
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-turkish.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-turkish.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Hyphenation patterns for Turkish in T1/EC and UTF-8 encodings. Auto-
generated from a script included in the distribution. The patterns for
Turkish were first produced for the Ottoman Texts Project in 1987 and
were suitable for both Modern Turkish and Ottoman Turkish in Latin
script, however the required character set didn't fit into EC encoding,
so support for Ottoman Turkish had to be dropped to keep compatibility
with 8-bit engines.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-turkish:
turkish loadhyph-tr.tex
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-turkish:
\addlanguage{turkish}{loadhyph-tr.tex}{}{2}{2}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-turkish:
['turkish'] = {
	loader = 'loadhyph-tr.tex',
	lefthyphenmin = 2,
	righthyphenmin = 2,
	synonyms = {  },
	patterns = 'hyph-tr.pat.txt',
},
TL_HYPHEN_EOF
