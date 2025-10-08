%%%%%%%%%%%%%%%%%
% This is altacv.cls (v1.7.4, 30 Jul 2025) written by
% LianTze Lim (liantze@gmail.com).
%
%% It may be distributed and/or modified under the
%% conditions of the LaTeX Project Public License, either version 1.3
%% of this license or (at your option) any later version.
%% The latest version of this license is in
%%    http://www.latex-project.org/lppl.txt
%% and version 1.3 or later is part of all distributions of LaTeX
%% version 2003/12/01 or later.
%%%%%%%%%%%%%%%%
\NeedsTeXFormat{LaTeX2e}[1995/12/01]
\ProvidesClass{altacv}[2025/07/30 AltaCV v1.7.4, yet another alternative class for a resume/curriculum vitae.]

\DeclareOption{academicons}{\ClassWarning{altacv}{academicons option is now obsolete and unnecessary.}}
\newif\if@normalphoto
\DeclareOption{normalphoto}{\@normalphototrue}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{extarticle}}
\newif\if@raggedtwoe
\DeclareOption{ragged2e}{\@raggedtwoetrue}
\newif\if@withhyper\@withhyperfalse
\DeclareOption{withhyper}{\@withhypertrue}
\ProcessOptions\relax

\LoadClass{extarticle}
\RequirePackage{etoolbox}
\newtoggle{withhyper}\togglefalse{withhyper}
\if@withhyper\toggletrue{withhyper}\fi
\RequirePackage{xcolor}
\RequirePackage[a-1b]{pdfx}
\RequirePackage{accsupp}
\pdfstringdefDisableCommands{
  \let\\\space
}
\RequirePackage{xparse}
\RequirePackage[margin=2cm]{geometry}
\RequirePackage[fixed]{fontawesome5}

\providecommand\IfFormatAtLeastTF{\@ifl@t@r\fmtversion}
\IfFormatAtLeastTF{2021-11-15}{}{\RequirePackage{scrlfile}}

\IfFileExists{simpleiconsglyphs-pdftex.tex}{\RequirePackage{simpleicons}}{}

\RequirePackage{iftex}
\ifundef{\iftutex}{%
  \newif\iftutex
  \ifxetex\tutextrue
  \else
    \ifluatex\tutextrue\else\tutexfalse\fi
  \fi
}{}
\iftutex 
  \RequirePackage{fontspec}
\else
  \RequirePackage{cmap}
  \RequirePackage[utf8]{inputenc}
  \RequirePackage[T1]{fontenc}
  \input{glyphtounicode}
  \pdfglyphtounicode{f_f}{FB00}
  \pdfglyphtounicode{f_f_i}{FB03}
  \pdfglyphtounicode{f_f_l}{FB04}
  \pdfglyphtounicode{f_i}{FB01}
  \pdfgentounicode=1
\fi

\if@raggedtwoe
  \RequirePackage[newcommands]{ragged2e}
\fi

\iftoggle{withhyper}{%
\IfFormatAtLeastTF{2020-10-01}{%
  \AddToHook{begindocument/before}{\hypersetup{hidelinks}\urlstyle{same}}
}{%
  \AtBeginDocument{\hypersetup{hidelinks}\urlstyle{same}}
}}{}

\colorlet{accent}{blue!70!black}
\colorlet{emphasis}{black}
\colorlet{heading}{black}
\colorlet{headingrule}{black}
\colorlet{subheading}{emphasis}
\colorlet{body}{black!80!white}
\colorlet{name}{heading}
\colorlet{tagline}{accent}
\newcommand{\cvItemMarker}{{\small\textbullet}}
\newcommand{\cvRatingMarker}{\faCircle}
\let\itemmarker\cvItemMarker
\let\ratingmarker\cvRatingMarker
\newcommand{\cvDateMarker}{\faCalendar[regular]}
\newcommand{\cvLocationMarker}{\faMapMarker}
\newcommand{\locationname}{Location}
\newcommand{\datename}{Date}

\RequirePackage{tikz}
\usetikzlibrary{arrows}
\RequirePackage[skins]{tcolorbox}
\RequirePackage[inline]{enumitem}
\setlist{leftmargin=*,labelsep=0.5em,nosep,itemsep=0.25\baselineskip,after=\vspace{0.25\baselineskip}}
\setlist[itemize]{label=\cvItemMarker}
\RequirePackage{graphicx}
\RequirePackage{trimclip}
\RequirePackage{dashrule}
\RequirePackage{multirow,tabularx}
\RequirePackage{changepage}

\setlength{\parindent}{0pt}
\newcommand{\divider}{\textcolor{body!30}{\hdashrule{\linewidth}{0.6pt}{0.5ex}}\medskip}

\newenvironment{fullwidth}{%
  \begin{adjustwidth}{}{\dimexpr-\marginparwidth-\marginparsep\relax}}
  {\end{adjustwidth}}

\newcommand{\utffriendlydetokenize}[1]{%
\scantokens{%
  \catcode`\_=12%
  \catcode`\&=12%
  \catcode`\$=12%
  \catcode`\#=12%
  \catcode`\~=12%
  {#1}%
}%
}

\ExplSyntaxOn
\NewDocumentCommand{\printinfo}{o m m o}{%
  \IfNoValueTF{#4}{%
    \mbox{\textcolor{accent}%
    {\BeginAccSupp{method=escape,ActualText={\IfNoValueTF{#1}{\detokenize{#2}}{#1}:\space}}\normalfont #2\EndAccSupp{}}%
    ~\utffriendlydetokenize{#3}\hspace{2em}}%
  }{%
    \iftoggle{withhyper}{%
      \mbox{\textcolor{accent}%
      {\BeginAccSupp{method=escape,ActualText={\IfNoValueTF{#1}{\detokenize{#2}}{#1}:\space}}\normalfont #2\EndAccSupp{}}%
      ~%
      \BeginAccSupp{method=escape,ActualText={#4}}%
      \href{#4}{\utffriendlydetokenize{#3}}%
      \EndAccSupp{}%
      \hspace{2em}}%
     }{%
       \ClassWarning{Please specify [withhyper] option to enable hyperlinks. Printing out full hyperlink prefix #1 for now.}%
      \mbox{\textcolor{accent}%
      {\BeginAccSupp{method=escape,ActualText={\IfNoValueTF{#1}{\detokenize{#2}}{#1}:\space}}\normalfont #2\EndAccSupp{}}%
      ~{\utffriendlydetokenize{#4}}\hspace{2em}}%
    }%
  }%
}%

\NewDocumentCommand{\NewInfoField}{s m m o}{%
  \IfBooleanF{#1}{%
    \IfNoValueTF{#4}%
      {\csdef{#2 hyperprefix}{}}%
      {\csdef{#2 hyperprefix}{#4}}%
  }%
  \csdef{#2 symbol}{#3}%
  \IfBooleanTF{#1}{%
    \csdef{#2}##1##2{%
        \if@withhyper%
          \IfNoValueTF{#4}%
            {\printinfo[#2]{#3}{##1}}%
            {\printinfo[#2]{#3}{##1}[##2]}%
        \else%
          \ClassWarning{altacv}{With withhyper=false, you should specify both arguments of \string\#2 that can be concatenated with the hyperlink prefix!}%
        \fi%
      }%
    }{%
      \csdef{#2}##1{%
          \if@withhyper%
            \IfNoValueTF{#4}%
              {\printinfo[#2]{#3}{##1}}%
              {\printinfo[#2]{#3}{##1}[\csuse{#2 hyperprefix}##1]}%
          \else%
            {\printinfo[#2]{\csuse{#2 symbol}}{##1}[\csuse{#2 hyperprefix}##1]}%
          \fi%
      }%
    }
}
\ExplSyntaxOff

\newcommand{\name}[1]{\def\@name{#1}}
\newcommand{\tagline}[1]{\def\@tagline{#1}}
\newcommand{\personalinfo}[1]{\def\@personalinfo{#1}}
\NewInfoField{email}{\faAt}[mailto:]
\NewInfoField{mailaddress}{\faEnvelope}
\NewInfoField{phone}{\faPhone}[tel:]
\NewInfoField{homepage}{\faGlobe}[https://]
\NewInfoField{twitter}{\faTwitter}[https://twitter.com/]
\ifcsdef{simpleicon@xicon}
 {\NewInfoField{xtwitter}{\raisebox{-0.2ex}{\scalebox{0.95}{\simpleicon{x}}}\,}[https://x.com/]}
 {\let\xtwitter\twitter%
  \pretocmd{\xtwitter}{\ClassWarning{altacv}{You tried to use \string\xtwitter, but the new X icon isn't available. Please ensure you have updated the `simpleicons' package. Falling back to \string\twitter\space icon for now}}{}{}%
 }
\NewInfoField{linkedin}{\faLinkedin}[https://linkedin.com/in/]
\NewInfoField{github}{\faGithub}[https://github.com/]
\ifdef{\faOrcid}{
  \NewInfoField{orcid}{\faOrcid}[https://orcid.org/]
}{\iftutex
    \RequirePackage{academicons}
    \NewInfoField{orcid}{\aiOrcid\space}[https://orcid.org/]
  \else
    \ClassWarning{altacv}{ORCID icon for \string\orcid\space unavailable in pdflatex. Please compile with XeLaTeX or LuaLaTeX; or upgrade your LaTeX distribution and packages}
    \NewInfoField{orcid}{\fbox{O?}\space}[https://orcid.org/]
  \fi
}
\NewInfoField{location}{\cvLocationMarker}

\newlength{\altacv@photos@width}
\newlength{\altacv@photo@diam@left}
\newlength{\altacv@photo@diam@right}
\def\altacv@left@photos{}
\def\altacv@right@photos{}

\newcommand{\@makeaphoto}[2]{%
  \begin{minipage}{#1}%
    \if@normalphoto
      \includegraphics[width=\linewidth]{#2}
    \else
      \tikz\path[fill overzoom image={#2}]circle[radius=0.5\linewidth];
    \fi%
  \end{minipage}%
}

\newcommand{\altacv@add@photo@left}[1]{%
  \appto{\altacv@left@photos}{%
    \@makeaphoto{\altacv@photo@diam@left}{#1}\hspace{1ex}%
  }%
  \addtolength{\altacv@photos@width}{\altacv@photo@diam@left}%
  \addtolength{\altacv@photos@width}{1ex}%
}
\newcommand{\altacv@add@photo@right}[1]{%
  \appto{\altacv@right@photos}{%
    \@makeaphoto{\altacv@photo@diam@right}{#1}\hspace{1ex}%
  }%
  \addtolength{\altacv@photos@width}{\altacv@photo@diam@right}%
  \addtolength{\altacv@photos@width}{1ex}%
}
\newcommand{\photoL}[2]{%
  \setlength{\altacv@photo@diam@left}{#1}%
  \forcsvlist{\altacv@add@photo@left}{#2}%
}
\newcommand{\photoR}[2]{%
  \setlength{\altacv@photo@diam@right}{#1}%
  \forcsvlist{\altacv@add@photo@right}{#2}%
}
\let\photo\photoR

\newcommand{\namefont}{\Huge\bfseries}
\newcommand{\taglinefont}{\large\bfseries}
\newcommand{\personalinfofont}{\footnotesize\bfseries}
\newcommand{\cvsectionfont}{\LARGE\bfseries}
\newcommand{\cvsubsectionfont}{\large\bfseries}

\newcommand{\makecvheader}{%
  \begingroup
    \altacv@left@photos\hfill%
    \begin{minipage}{\dimexpr\linewidth-\altacv@photos@width}%
    \raggedright%
    {\namefont\color{name}\MakeUppercase{\@name}\par}
    \medskip
    {\taglinefont\color{tagline}\@tagline\par}
    \medskip
    {\personalinfofont\@personalinfo\par}
    \end{minipage}\hfill%
    \altacv@right@photos\par%
  \endgroup\medskip
}

\renewenvironment{quote}{\color{accent}\itshape\large}{\par}

\newcommand{\cvsection}[2][]{%
  \nointerlineskip\bigskip%
  \ifstrequal{#1}{}{}{\marginpar{\vspace*{\dimexpr1pt-\baselineskip}\raggedright\input{#1}}}%
  {\color{heading}\cvsectionfont\MakeUppercase{#2}}\\[-1ex]%
  {\color{headingrule}\rule{\linewidth}{2pt}\par}\medskip
}

\newcommand{\cvsubsection}[1]{%
  \smallskip%
  {\color{subheading}\cvsubsectionfont{#1}\par}\medskip
}

\newcommand{\cvevent}[4]{%
  {\large\color{emphasis}#1\par}
  \smallskip\normalsize
  \ifstrequal{#2}{}{}{
  \textbf{\color{accent}#2}\par
  \smallskip}
  \ifstrequal{#3}{}{}{%
    {\small\makebox[0.5\linewidth][l]%
      {\BeginAccSupp{method=pdfstringdef,ActualText={\datename:}}\cvDateMarker\EndAccSupp{}%
      ~#3}%
    }}%
  \ifstrequal{#4}{}{}{%
    {\small\makebox[0.5\linewidth][l]%
      {\BeginAccSupp{method=pdfstringdef,ActualText={\locationname:}}\cvLocationMarker\EndAccSupp{}%
        ~#4}%
    }}\par
  \medskip\normalsize
}

\newcommand{\cvachievement}[3]{%
  \begin{tabularx}{\linewidth}{@{}p{2em} @{\hspace{1ex}} >{\raggedright\arraybackslash}X@{}}
  \multirow{2}{*}{\Large\color{accent}\BeginAccSupp{method=escape,ActualText={#1: }}#1\EndAccSupp{}} & \bfseries\textcolor{emphasis}{#2}\\
  & #3
  \end{tabularx}%
  \smallskip
}

\newcommand{\cvtag}[1]{%
  \tikz[baseline]\node[anchor=base,draw=body!30,rounded corners,inner xsep=1ex,inner ysep =0.75ex,text height=1.5ex,text depth=.25ex]{#1};
}

\newcommand{\cvskill}[2]{%
  \textcolor{emphasis}{\textbf{#1}}\hfill
  \BeginAccSupp{method=plain,ActualText={#2}}
  \foreach \x in {1,...,5}{%
    \ifdimequal{\x pt - #2 pt}{0.5pt}%
    {\clipbox*{0pt -0.25ex {.5\width} {\totalheight}}{\color{accent}\cvRatingMarker}%
     \clipbox*{{.5\width} -0.25ex {\width} {\totalheight}}{\color{body!30}\cvRatingMarker}}
    {\ifdimgreater{\x bp}{#2 bp}{\color{body!30}}{\color{accent}}\cvRatingMarker}%
  }\EndAccSupp{}\par%
}

\newcommand{\wheelchart}[4][0]{%
    \begingroup\centering
    \def\innerradius{#3}%
    \def\outerradius{#2}%
    \pgfmathsetmacro{\totalnum}{0}%
    \foreach \value/\colour/\name in {#4} {%
        \pgfmathparse{\value+\totalnum}%
        \global\let\totalnum=\pgfmathresult%
    }%
    \begin{tikzpicture}

      \pgfmathsetmacro{\wheelwidth}{\outerradius-\innerradius}
      \pgfmathsetmacro{\midradius}{(\outerradius+\innerradius)/2}
      \pgfmathsetmacro{\totalrot}{-90 + #1}

      \begin{scope}[rotate=\totalrot]

      \pgfmathsetmacro{\cumnum}{0}
      \foreach \value/\width/\colour/\name in {#4} {
            \pgfmathsetmacro{\newcumnum}{\cumnum + \value/\totalnum*360}

            \pgfmathsetmacro{\percentage}{\value/\totalnum*100}
            \pgfmathsetmacro{\midangle}{-(\cumnum+\newcumnum)/2}

            \pgfmathparse{
               (-\midangle>180?"west":"east")
            } \edef\textanchor{\pgfmathresult}
            \pgfmathparse{
               (-\midangle>180?"flush left":"flush right")
            } \edef\textalign{\pgfmathresult}
            \pgfmathsetmacro\labelshiftdir{1-2*(-\midangle<180)}

            \filldraw[draw=white,fill=\colour] (-\cumnum:\outerradius) arc (-\cumnum:-(\newcumnum):\outerradius) --
            (-\newcumnum:\innerradius) arc (-\newcumnum:-(\cumnum):\innerradius) -- cycle;

            \draw  [*-,thin,emphasis] node [append after command={(\midangle:\midradius pt) -- (\midangle:\outerradius + 1ex) -- (\tikzlastnode)}] at (\midangle:\outerradius + 1ex) [xshift=\labelshiftdir*0.5cm,inner sep=1ex, outer sep=0pt, text width=\width,anchor=\textanchor,align=\textalign,font=\small,text=body]{\BeginAccSupp{method=pdfstringdef,ActualText={\name: \value}}\name\EndAccSupp{}};
            \global\let\cumnum=\newcumnum
        }
      \end{scope}
    \end{tikzpicture}\par
    \endgroup
}

\newcommand{\cvref}[3]{%
  \smallskip
  \textcolor{emphasis}{\textbf{#1}}\par
  \begin{description}[font=\color{accent},style=multiline,leftmargin=1.35em,align=left]
  \item[\small\normalfont\emailsymbol] #2
  \item[\small\normalfont\mailaddresssymbol] #3
  \end{description}
}

\newenvironment{cvcolumn}[1]{\begin{minipage}[t]{#1}\raggedright}{\end{minipage}}

\RequirePackage{afterpage}
\newcommand{\addsidebar}[2][]{\marginpar{%
  \ifstrequal{#1}{}{}{\vspace*{#1}}%
  \input{#2}}%
}
\newcommand{\addnextpagesidebar}[2][]{\afterpage{\addsidebar[#1]{#2}}}

\RequirePackage{pgffor}
\def\my@namelist{}
\newcommand{\mynames}[1]{\def\my@namelist{#1}}
\newtoggle{boldname}
\IfFormatAtLeastTF{2021-11-15}{%
  \AddToHook{package/biblatex/after}{%
    \typeout{OK AddToHook biblatex after works}
    \altacv@makeboldnames
  }%
}{%
  \AfterPackage{biblatex}{%
    \typeout{OK AfterPackage biblatex after works}
    \altacv@makeboldnames
  }%
}

\newcommand{\altacv@makeboldnames}{%
  \renewcommand*{\mkbibnamefamily}[1]{%
    \global\togglefalse{boldname}%
    \foreach \my@fname / \my@gname in \my@namelist {%
      \ifboolexpr{ test {\ifdefstrequal{\namepartfamily}{\my@fname}}
                   and
                   test {\ifdefstrequal{\namepartgiven}{\my@gname}}}
        {\global\toggletrue{boldname}}{}%
    }%
    \iftoggle{boldname}{\textbf{##1}}{##1}%
  }%
  \let\mkbibnamegiven\mkbibnamefamily%
  \let\mkbibnameprefix\mkbibnamefamily%
  \let\mkbibnamesuffix\mkbibnamefamily%
}

\IfFormatAtLeastTF{2020-10-01}{%
  \AddToHook{begindocument/before}{%
    \pagestyle{empty}%
    \color{body}%
    \raggedright%
  }
}{%
  \AtBeginDocument{%
    \pagestyle{empty}%
    \color{body}%
    \raggedright%
  }
}
