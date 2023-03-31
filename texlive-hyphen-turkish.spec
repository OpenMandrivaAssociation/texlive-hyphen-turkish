Name:		texlive-hyphen-turkish
Version:	58652
Release:	2
Summary:	Turkish hyphenation patterns
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/hyphenation/tkhyph.tex
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-turkish.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Turkish in T1/EC and UTF-8 encodings.
The patterns for Turkish were first produced for the Ottoman
Texts Project in 1987 and were suitable for both Modern Turkish
and Ottoman Turkish in Latin script, however the required
character set didn't fit into EC encoding, so support for
Ottoman Turkish had to be dropped to keep compatibility with 8-
bit engines.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/*
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/*/*
%_texmf_language_dat_d/hyphen-turkish
%_texmf_language_def_d/hyphen-turkish
%_texmf_language_lua_d/hyphen-turkish

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}

mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-turkish <<EOF
\%% from hyphen-turkish:
turkish loadhyph-tr.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-turkish
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-turkish <<EOF
\%% from hyphen-turkish:
\addlanguage{turkish}{loadhyph-tr.tex}{}{2}{2}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-turkish
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-turkish <<EOF
-- from hyphen-turkish:
	['turkish'] = {
		loader = 'loadhyph-tr.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-tr.pat.txt',
		hyphenation = '',
	},
EOF
