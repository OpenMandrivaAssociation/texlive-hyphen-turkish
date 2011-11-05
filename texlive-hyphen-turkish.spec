# revision 23085
# category TLCore
# catalog-ctan /language/hyphenation/tkhyph.tex
# catalog-date 2011-02-23 08:51:21 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-hyphen-turkish
Version:	20110223
Release:	1
Summary:	Turkish hyphenation patterns
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/hyphenation/tkhyph.tex
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-turkish.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8
Conflicts:	texlive-texmf <= 20110705-3

%description
Hyphenation patterns for Turkish in T1/EC and UTF-8 encodings.
The patterns for Turkish were first produced for the Ottoman
Texts Project in 1987 and were suitable for both Modern Turkish
and Ottoman Turkish in Latin script, however the required
character set didn't fit into EC encoding, so support for
Ottoman Turkish had to be dropped to keep compatibility with 8-
bit engines.

%pre
    %_texmf_language_dat_pre
    %_texmf_language_def_pre
    %_texmf_language_lua_pre

%post
    %_texmf_language_dat_post
    %_texmf_language_def_post
    %_texmf_language_lua_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_language_dat_pre
	%_texmf_language_def_pre
	%_texmf_language_lua_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_language_dat_post
	%_texmf_language_def_post
	%_texmf_language_lua_post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-turkish
%_texmf_language_def_d/hyphen-turkish
%_texmf_language_lua_d/hyphen-turkish
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-turkish <<EOF
%% from hyphen-turkish:
turkish loadhyph-tr.tex
EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-turkish <<EOF
%% from hyphen-turkish:
\addlanguage{turkish}{loadhyph-tr.tex}{}{2}{2}
EOF
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
