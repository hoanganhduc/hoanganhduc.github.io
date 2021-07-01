<?xml version="1.0" encoding="utf-8"?>
<!--
/=====================================================================\ 
|  LaTeXML-webpage-xhtml.xsl                                          |
|  General purpose webpage wrapper for LaTeXML documents in xhtml     |
|=====================================================================|
| Part of LaTeXML:                                                    |
|  Public domain software, produced as part of work done by the       |
|  United States Government & not subject to copyright in the US.     |
|=====================================================================|
| Bruce Miller <bruce.miller@nist.gov>                        #_#     |
| http://dlmf.nist.gov/LaTeXML/                              (o o)    |
\=========================================================ooo==U==ooo=/
-->
<xsl:stylesheet
    version     = "1.0"
    xmlns:xsl   = "http://www.w3.org/1999/XSL/Transform"
    xmlns:ltx   = "http://dlmf.nist.gov/LaTeXML"
    xmlns:string= "http://exslt.org/strings"
    xmlns:f     = "http://dlmf.nist.gov/LaTeXML/functions"
    xmlns:m     = "http://www.w3.org/1998/Math/MathML"
    exclude-result-prefixes = "ltx f"
    extension-element-prefixes="string f">

  <!-- We don't really anticipate page structure appearing in inline contexts,
       so we pretty much ignore the $context switches.
       See the CONTEXT discussion in LaTeXML-common -->

  <!--  ======================================================================
       The Page
       ====================================================================== -->

  <!-- This schematic gives an indication of the default page structure.
       You can, of course, use CSS to lay it out differently!
       <html>
         <head>...</head>
         <body>
           <div class="ltx_page_navbar>...</div>
           <div class="ltx_page_main">
             <div class="ltx_page_header">
               header navigation
             </div>
             <div class="ltx_page_content">
               Your Document Here!
               ...
             </div>
             <div class="ltx_page_footer">
               footer navigation
               LaTeXML logo
             </div>
           </div>
         </body>
       </html>
  -->
  <!-- This version generates MathML & SVG with an xmlns namespace declaration 
       on EACH math/svg node;
       If you want to declare and use namespace prefixes (m & svg, resp), add this here
       xmlns:m   = "http://www.w3.org/1998/Math/MathML"
       xmlns:svg = "http://www.w3.org/2000/svg"
       and change local-name() to name() in LaTeXML-math-mathml & LaTeXML-picture-svg.
       NOTE: Can I make a template to add namespace prefix declarations here?
       Then $USE_NAMESPACES .. ? Do the experiment!!
  -->

  <!--  ======================================================================
       The <body>
       ====================================================================== -->

  <xsl:template match="/" mode="body">
    <xsl:text>&#x0A;</xsl:text>
    <xsl:element name="body" namespace="{$html_ns}">
      <xsl:apply-templates select="." mode="body-begin"/>
      <xsl:apply-templates select="." mode="navbar"/>
      <xsl:apply-templates select="." mode="body-main"/>
      <xsl:apply-templates select="." mode="body-end"/>
      <xsl:text>&#x0A;</xsl:text>
    </xsl:element>
  </xsl:template>

  <xsl:template match="/" mode="body-begin"/>
  <xsl:template match="/" mode="body-end"/>

  <xsl:template match="/" mode="body-main">
    <xsl:text>&#x0A;</xsl:text>
    <xsl:element name="div" namespace="{$html_ns}">
      <xsl:attribute name="class">ltx_page_main</xsl:attribute>
      <xsl:apply-templates select="." mode="body-main-begin"/>
      <xsl:apply-templates select="." mode="header"/>
      <xsl:apply-templates select="." mode="body-content"/>
      <xsl:apply-templates select="." mode="footer"/>
      <xsl:apply-templates select="." mode="body-main-end"/>
      <xsl:text>&#x0A;</xsl:text>
    </xsl:element>
  </xsl:template>

  <xsl:template match="/" mode="body-main-begin"/>
  <xsl:template match="/" mode="body-main-end"/>

  <xsl:template match="/" mode="body-content">
    <xsl:text>&#x0A;</xsl:text>
    <xsl:element name="div" namespace="{$html_ns}">
      <xsl:attribute name="class">ltx_page_content</xsl:attribute>
      <xsl:apply-templates select="." mode="body-content-begin"/>
      <xsl:apply-templates/>
      <xsl:apply-templates select="." mode="body-content-end"/>
      <xsl:text>&#x0A;</xsl:text>
    </xsl:element>
  </xsl:template>

  <xsl:template match="/" mode="body-content-begin"/>
  <xsl:template match="/" mode="body-content-end"/>

  <!--  ======================================================================
       Tables of Contents.
       ====================================================================== -->

  <xsl:strip-space elements="ltx:TOC ltx:toclist ltx:tocentry"/>
  <xsl:template match="ltx:TOC/ltx:title"/>

  <!-- explicitly requested TOC -->
  <xsl:template match="ltx:TOC[@format='short']">
    <xsl:param name="context"/>
    <xsl:element name="div" namespace="{$html_ns}">
      <xsl:call-template name='add_attributes'>
        <xsl:with-param name="extra_classes" select="f:class-pref('ltx_toc_',@lists)"/>
      </xsl:call-template>
      <xsl:apply-templates mode="short">
        <xsl:with-param name="context" select="$context"/>
      </xsl:apply-templates>
    </xsl:element>
  </xsl:template>

  <xsl:template match="ltx:TOC[@format='veryshort']">
    <xsl:param name="context"/>
    <xsl:element name="div" namespace="{$html_ns}">
      <xsl:call-template name='add_attributes'>
        <xsl:with-param name="extra_classes" select="f:class-pref('ltx_toc_',@lists)"/>
      </xsl:call-template>
      <xsl:apply-templates mode="veryshort">
        <xsl:with-param name="context" select="$context"/>
      </xsl:apply-templates>
    </xsl:element>
  </xsl:template>

  <xsl:template match="ltx:TOC[@format='normal2']">
    <xsl:param name="context"/>
    <xsl:element name="div" namespace="{$html_ns}">
      <xsl:call-template name='add_attributes'>
        <xsl:with-param name="extra_classes" select="f:class-pref('ltx_toc_',@lists)"/>
      </xsl:call-template>
      <xsl:apply-templates mode="normal2">
        <xsl:with-param name="context" select="$context"/>
      </xsl:apply-templates>
    </xsl:element>
  </xsl:template>

  <xsl:template match="ltx:TOC">
    <xsl:param name="context"/>
    <xsl:if test="ltx:toclist/descendant::ltx:tocentry">
      <xsl:text>&#x0A;</xsl:text>
      <xsl:element name="div" namespace="{$html_ns}">
        <xsl:call-template name='add_attributes'>
          <xsl:with-param name="extra_classes" select="f:class-pref('ltx_toc_',@lists)"/>
        </xsl:call-template>
        <xsl:if test="ltx:title">
          <xsl:element name="h2" namespace="{$html_ns}">
            <xsl:variable name="innercontext" select="'inline'"/><!-- override -->
            <xsl:apply-templates select="ltx:title/node()">
              <xsl:with-param name="context" select="$innercontext"/>
            </xsl:apply-templates>
          </xsl:element>
        </xsl:if>
        <xsl:apply-templates>
          <xsl:with-param name="context" select="$context"/>
        </xsl:apply-templates>
      </xsl:element>
    </xsl:if>
  </xsl:template>

  <xsl:template match="ltx:toclist" mode="short">
    <xsl:param name="context"/>
    <xsl:text>&#x0A;</xsl:text>
    <xsl:element name="div" namespace="{$html_ns}">
      <xsl:call-template name='add_attributes'>
        <xsl:with-param name="extra_classes" select="'ltx_toc_compact'"/>
      </xsl:call-template>
      <xsl:text>&#x0A;&#x2666; </xsl:text>
      <xsl:apply-templates mode="short">
        <xsl:with-param name="context" select="$context"/>
      </xsl:apply-templates>
    </xsl:element>
  </xsl:template>

  <xsl:template match="ltx:toclist" mode="veryshort">
    <xsl:param name="context"/>
    <xsl:text>&#x0A;</xsl:text>
    <xsl:element name="div" namespace="{$html_ns}">
      <xsl:call-template name='add_attributes'>
        <xsl:with-param name="extra_classes" select="'ltx_toc_verycompact'"/>
      </xsl:call-template>
      <xsl:text>&#x2666;</xsl:text>
      <xsl:apply-templates mode="veryshort">
        <xsl:with-param name="context" select="$context"/>
      </xsl:apply-templates>
    </xsl:element>
  </xsl:template>

  <xsl:template match="ltx:toclist">
    <xsl:param name="context"/>
    <xsl:text>&#x0A;</xsl:text>
    <xsl:element name="ul" namespace="{$html_ns}">
      <xsl:call-template name='add_id'/>
      <xsl:call-template name='add_attributes'/>
<!--      <xsl:attribute name="class">ltx_toclist list-group list-group-flush</xsl:attribute>-->
      <xsl:apply-templates>
        <xsl:with-param name="context" select="$context"/>
      </xsl:apply-templates>
      <xsl:text>&#x0A;</xsl:text>
    </xsl:element>
  </xsl:template>

  <xsl:template match="ltx:toclist" mode="normal2">
    <xsl:param name="context"/>
    <xsl:text>&#x0A;</xsl:text>
    <xsl:apply-templates select="." mode="twocolumn">
      <xsl:with-param name="context" select="$context"/>
    </xsl:apply-templates>
  </xsl:template>
  <xsl:template match="ltx:toclist" mode="twocolumn">
    <xsl:param name="context"/>
    <xsl:param name="items"    select="ltx:tocentry"/>
    <xsl:param name="lines"    select="descendant::ltx:tocentry"/>
    <xsl:param name="halflines" select="ceiling(count($lines) div 2)"/>
    <xsl:param name="miditem"
               select="count($lines[position() &lt; $halflines]/ancestor::ltx:tocentry[parent::ltx:toclist[parent::ltx:TOC]]) + 1"/>
    <xsl:call-template name="split-columns">
      <xsl:with-param name="context" select="$context"/>
      <xsl:with-param name="wrapper" select="'ul'"/>
      <xsl:with-param name="items"   select="$items"/>
      <xsl:with-param name="miditem" select="$miditem"/>
    </xsl:call-template>
  </xsl:template>

  <xsl:template match="ltx:tocentry">
    <xsl:param name="context"/>
    <xsl:text>&#x0A;</xsl:text>
    <xsl:element name="li" namespace="{$html_ns}">
      <xsl:call-template name='add_id'/>
      <xsl:call-template name='add_attributes'/>
<!--      <xsl:attribute name="class">ltx_tocentry ltx_tocentry_section list-group-item</xsl:attribute>-->
      <xsl:apply-templates>
        <xsl:with-param name="context" select="$context"/>
      </xsl:apply-templates>
    </xsl:element>
  </xsl:template>

  <xsl:template match="ltx:tocentry" mode="short">
    <xsl:param name="context"/>
    <xsl:apply-templates>
      <xsl:with-param name="context" select="$context"/>
    </xsl:apply-templates>
    <xsl:text> &#x2666; </xsl:text>
  </xsl:template>

  <xsl:template match="ltx:tocentry" mode="veryshort">
    <xsl:param name="context"/>
    <xsl:apply-templates>
      <xsl:with-param name="context" select="$context"/>
    </xsl:apply-templates>
    <xsl:text>&#x2666;</xsl:text>
  </xsl:template>

</xsl:stylesheet>
