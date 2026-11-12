# -*- coding: utf-8 -*-
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def create_workshop_doc():
    doc = docx.Document()

    # 1. Page setup - Margins (2 cm / 0.79 in)
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)
        section.page_width = Inches(8.5)
        section.page_height = Inches(11.0)

    # Palette
    COLOR_PRIMARY = RGBColor(15, 44, 89)      # #0F2C59 - Deep Navy Blue
    COLOR_SECONDARY = RGBColor(26, 115, 232)  # #1A73E8 - Professional Blue
    COLOR_DARK = RGBColor(30, 41, 59)         # #1E293B - Slate Dark Text
    COLOR_MUTED = RGBColor(100, 116, 139)     # #64748B - Gray Subtitle
    COLOR_HIGHLIGHT = RGBColor(194, 65, 12)   # #C2410C - Amber/Orange alert

    HEX_PRIMARY = "0F2C59"
    HEX_SECONDARY = "1A73E8"
    HEX_LIGHT_BG = "F8FAFC"
    HEX_BORDER = "CBD5E1"
    HEX_CMD_BG = "0F172A"       # Dark terminal background
    HEX_CMD_TXT = "38BDF8"      # Terminal cyan
    HEX_ALERT_BG = "FEF3C7"     # Warning light yellow
    HEX_ALERT_BORDER = "F59E0B"
    HEX_STUDENT_BG = "F1F5F9"   # Student response light gray

    # Set normal style font
    style_normal = doc.styles['Normal']
    style_normal.font.name = 'Segoe UI'
    style_normal.font.size = Pt(10.5)
    style_normal.font.color.rgb = COLOR_DARK

    def set_cell_background(cell, hex_color):
        tcPr = cell._element.get_or_add_tcPr()
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
        tcPr.append(shd)

    def set_cell_margins(cell, top=140, bottom=140, left=180, right=180):
        tcPr = cell._element.get_or_add_tcPr()
        tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}>'
                          f'<w:top w:w="{top}" w:type="dxa"/>'
                          f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
                          f'<w:left w:w="{left}" w:type="dxa"/>'
                          f'<w:right w:w="{right}" w:type="dxa"/>'
                          f'</w:tcMar>')
        tcPr.append(tcMar)

    def set_cell_borders(cell, top="none", bottom="none", left="none", right="none", 
                         color="CBD5E1", sz="4"):
        tcPr = cell._element.get_or_add_tcPr()
        tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}>'
                              f'<w:top w:val="{top}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                              f'<w:left w:val="{left}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                              f'<w:bottom w:val="{bottom}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                              f'<w:right w:val="{right}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                              f'</w:tcBorders>')
        tcPr.append(tcBorders)

    def add_header_block():
        # Top banner table
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        tbl.columns[0].width = Inches(6.9)
        cell = tbl.cell(0, 0)
        set_cell_background(cell, HEX_PRIMARY)
        set_cell_margins(cell, top=200, bottom=200, left=240, right=240)
        set_cell_borders(cell, top="single", bottom="single", left="single", right="single", color=HEX_PRIMARY, sz="12")

        p0 = cell.paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p0.paragraph_format.space_before = Pt(0)
        p0.paragraph_format.space_after = Pt(2)
        r0 = p0.add_run("INSTITUTO SUPERIOR TECNOLÓGICO YAVIRAC")
        r0.bold = True
        r0.font.size = Pt(14)
        r0.font.color.rgb = RGBColor(255, 255, 255)

        p1 = cell.add_paragraph()
        p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p1.paragraph_format.space_before = Pt(0)
        p1.paragraph_format.space_after = Pt(4)
        r1 = p1.add_run("CARRERA DE DESARROLLO DE SOFTWARE | TENDENCIAS ACTUALES DE PROGRAMACIÓN")
        r1.font.size = Pt(10)
        r1.font.bold = True
        r1.font.color.rgb = RGBColor(219, 234, 254)

        p2 = cell.add_paragraph()
        p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p2.paragraph_format.space_before = Pt(4)
        p2.paragraph_format.space_after = Pt(0)
        r2 = p2.add_run("GUÍA DE TALLER PRÁCTICO EVALUATORIO")
        r2.bold = True
        r2.font.size = Pt(13)
        r2.font.color.rgb = RGBColor(255, 215, 0) # Gold accent

        doc.add_paragraph().paragraph_format.space_after = Pt(4)

    def add_meta_table():
        tbl = doc.add_table(rows=4, cols=4)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False

        col_widths = [Inches(1.5), Inches(2.2), Inches(1.3), Inches(1.9)]
        for row in tbl.rows:
            for i, w in enumerate(col_widths):
                row.cells[i].width = w

        data = [
            [("ESTUDIANTE:", True), ("________________________________________", False), 
             ("FECHA:", True), ("____ / ____ / 2026", False)],
            [("NIVEL / PARALELO:", True), ("________________________", False), 
             ("ASIGNATURA:", True), ("Tendencias Actuales de Prog.", False)],
            [("DOCENTE:", True), ("Ing. Byron (Cátedra)", False), 
             ("SERVIDOR DESTINO:", True), ("161.97.140.245 (Linux)", True)],
            [("TEMA DEL TALLER:", True), ("Despliegue de Servicios con Docker en Servidor Remoto (v1 y v2)", False), 
             ("CALIFICACIÓN:", True), ("________ / 10.00 pts", True)]
        ]

        for r_idx, row_data in enumerate(data):
            for c_idx, cell_info in enumerate(row_data):
                cell = tbl.cell(r_idx, c_idx)
                set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
                set_cell_borders(cell, top="single", bottom="single", left="single", right="single", color=HEX_BORDER, sz="4")
                p = cell.paragraphs[0]
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.space_after = Pt(0)
                txt, is_bold = cell_info
                run = p.add_run(txt)
                run.bold = is_bold
                run.font.size = Pt(9.5)
                if c_idx in [0, 2]:
                    set_cell_background(cell, "F1F5F9")
                    run.font.color.rgb = COLOR_PRIMARY
                else:
                    run.font.color.rgb = COLOR_DARK

        doc.add_paragraph().paragraph_format.space_after = Pt(6)

    def add_section_title(number_str, title_str):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        
        r_num = p.add_run(number_str + " ")
        r_num.bold = True
        r_num.font.size = Pt(12)
        r_num.font.color.rgb = COLOR_SECONDARY
        
        r_title = p.add_run(title_str.upper())
        r_title.bold = True
        r_title.font.size = Pt(12)
        r_title.font.color.rgb = COLOR_PRIMARY

        # Add a subtle bottom border/rule
        pBrd = parse_xml(f'<w:pBrd {nsdecls("w")}><w:bottom w:val="single" w:sz="6" w:space="2" w:color="{HEX_SECONDARY}"/></w:pBrd>')
        p._p.get_or_add_pPr().append(pBrd)

    def add_callout(title, text, alert_type="info"):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        tbl.columns[0].width = Inches(6.9)
        cell = tbl.cell(0, 0)

        if alert_type == "warning":
            bg = HEX_ALERT_BG
            b_color = HEX_ALERT_BORDER
            title_color = RGBColor(180, 83, 9)
        elif alert_type == "important":
            bg = "EFF6FF"
            b_color = "2563EB"
            title_color = RGBColor(29, 78, 216)
        else:
            bg = HEX_LIGHT_BG
            b_color = HEX_SECONDARY
            title_color = COLOR_PRIMARY

        set_cell_background(cell, bg)
        set_cell_margins(cell, top=100, bottom=100, left=150, right=150)
        set_cell_borders(cell, top="none", bottom="none", left="single", right="none", color=b_color, sz="24")

        p0 = cell.paragraphs[0]
        p0.paragraph_format.space_before = Pt(0)
        p0.paragraph_format.space_after = Pt(2)
        r_t = p0.add_run(f"📌 {title}: ")
        r_t.bold = True
        r_t.font.size = Pt(10)
        r_t.font.color.rgb = title_color

        r_body = p0.add_run(text)
        r_body.font.size = Pt(9.5)
        r_body.font.color.rgb = COLOR_DARK

        doc.add_paragraph().paragraph_format.space_after = Pt(4)

    def add_explanation_box(prompt_title, guidance_text, min_lines=5):
        tbl = doc.add_table(rows=2, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        tbl.columns[0].width = Inches(6.9)

        # Header of box
        c0 = tbl.cell(0, 0)
        set_cell_background(c0, "E2E8F0")
        set_cell_margins(c0, top=60, bottom=60, left=100, right=100)
        set_cell_borders(c0, top="single", bottom="single", left="single", right="single", color=HEX_BORDER, sz="6")
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_before = Pt(0)
        p0.paragraph_format.space_after = Pt(0)
        r0 = p0.add_run(f"📝 {prompt_title}")
        r0.bold = True
        r0.font.size = Pt(9.5)
        r0.font.color.rgb = COLOR_PRIMARY

        # Body for student to fill
        c1 = tbl.cell(1, 0)
        set_cell_background(c1, "FAFAFA")
        set_cell_margins(c1, top=100, bottom=100, left=120, right=120)
        set_cell_borders(c1, top="none", bottom="single", left="single", right="single", color=HEX_BORDER, sz="6")
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_before = Pt(0)
        p1.paragraph_format.space_after = Pt(4)
        r_guide = p1.add_run(f"Instrucción para el estudiante: {guidance_text}\n")
        r_guide.font.italic = True
        r_guide.font.size = Pt(8.5)
        r_guide.font.color.rgb = COLOR_MUTED

        # Insert placeholder lines
        for _ in range(min_lines):
            p_line = c1.add_paragraph()
            p_line.paragraph_format.space_before = Pt(0)
            p_line.paragraph_format.space_after = Pt(2)
            r_dot = p_line.add_run("____________________________________________________________________________________")
            r_dot.font.color.rgb = RGBColor(203, 213, 225)
            r_dot.font.size = Pt(9)

        doc.add_paragraph().paragraph_format.space_after = Pt(4)

    def add_command_box(title, instructions, placeholder_cmd=""):
        tbl = doc.add_table(rows=2, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        tbl.columns[0].width = Inches(6.9)

        # Header
        c0 = tbl.cell(0, 0)
        set_cell_background(c0, "1E293B") # dark slate
        set_cell_margins(c0, top=60, bottom=60, left=100, right=100)
        set_cell_borders(c0, top="single", bottom="none", left="single", right="single", color="1E293B", sz="6")
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_before = Pt(0)
        p0.paragraph_format.space_after = Pt(0)
        r0 = p0.add_run(f"💻 COMANDOS UTILIZADOS: {title}")
        r0.bold = True
        r0.font.size = Pt(9.5)
        r0.font.color.rgb = RGBColor(248, 250, 252)

        # Terminal area
        c1 = tbl.cell(1, 0)
        set_cell_background(c1, "0F172A") # deep terminal black
        set_cell_margins(c1, top=100, bottom=100, left=120, right=120)
        set_cell_borders(c1, top="none", bottom="single", left="single", right="single", color="1E293B", sz="6")
        
        p_instr = c1.paragraphs[0]
        p_instr.paragraph_format.space_before = Pt(0)
        p_instr.paragraph_format.space_after = Pt(4)
        r_i = p_instr.add_run(f"# {instructions}\n")
        r_i.font.name = "Consolas"
        r_i.font.size = Pt(8.5)
        r_i.font.color.rgb = RGBColor(148, 163, 184) # slate comment

        # Default or blank lines for student code
        p_code = c1.add_paragraph()
        p_code.paragraph_format.space_before = Pt(0)
        p_code.paragraph_format.space_after = Pt(2)
        if placeholder_cmd:
            r_c = p_code.add_run(placeholder_cmd + "\n")
            r_c.font.name = "Consolas"
            r_c.font.size = Pt(9.5)
            r_c.font.color.rgb = RGBColor(56, 189, 248) # cyan
        
        # extra empty lines
        for _ in range(2):
            p_empty = c1.add_paragraph()
            p_empty.paragraph_format.space_before = Pt(0)
            p_empty.paragraph_format.space_after = Pt(2)
            r_e = p_empty.add_run("$ ")
            r_e.font.name = "Consolas"
            r_e.font.size = Pt(9.5)
            r_e.font.color.rgb = RGBColor(52, 211, 153) # green prompt

        doc.add_paragraph().paragraph_format.space_after = Pt(4)

    def add_screenshot_box(evidence_title, note):
        tbl = doc.add_table(rows=2, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        tbl.columns[0].width = Inches(6.9)

        # Header
        c0 = tbl.cell(0, 0)
        set_cell_background(c0, "DBEAFE") # Light blue
        set_cell_margins(c0, top=60, bottom=60, left=100, right=100)
        set_cell_borders(c0, top="single", bottom="single", left="single", right="single", color="93C5FD", sz="6")
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_before = Pt(0)
        p0.paragraph_format.space_after = Pt(0)
        r0 = p0.add_run(f"📷 EVIDENCIA FOTOGRÁFICA: {evidence_title}")
        r0.bold = True
        r0.font.size = Pt(9.5)
        r0.font.color.rgb = RGBColor(30, 64, 175)

        # Body box
        c1 = tbl.cell(1, 0)
        set_cell_background(c1, "F8FAFC")
        set_cell_margins(c1, top=140, bottom=140, left=120, right=120)
        set_cell_borders(c1, top="none", bottom="single", left="single", right="single", color="93C5FD", sz="6")
        
        p1 = c1.paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p1.paragraph_format.space_before = Pt(12)
        p1.paragraph_format.space_after = Pt(4)
        r1 = p1.add_run("┌────────────────────────────────────────────────────────┐\n"
                        "│        [PEGAR AQUÍ LA CAPTURA DE PANTALLA CLARA Y LEGIBLE]        │\n"
                        "└────────────────────────────────────────────────────────┘")
        r1.font.name = "Consolas"
        r1.font.size = Pt(9)
        r1.font.color.rgb = RGBColor(148, 163, 184)

        p2 = c1.add_paragraph()
        p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p2.paragraph_format.space_before = Pt(4)
        p2.paragraph_format.space_after = Pt(12)
        r2 = p2.add_run(f"Nota de validación: {note}")
        r2.font.italic = True
        r2.font.size = Pt(8.5)
        r2.font.color.rgb = COLOR_MUTED

        doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # ==================== DOCUMENT CONTENT ====================
    add_header_block()
    add_meta_table()

    # SECTION 1
    add_section_title("1.", "Objetivo General y Alcance del Taller")
    p_obj = doc.add_paragraph()
    p_obj.paragraph_format.space_before = Pt(2)
    p_obj.paragraph_format.space_after = Pt(4)
    p_obj.add_run(
        "El objetivo primordial del presente taller es desplegar un servicio web o API desarrollado en el lenguaje de "
        "programación de su elección (Python, Node.js, Java, Go, PHP, etc.) dentro de un único contenedor Docker "
        "en el servidor remoto del laboratorio institucional ("
    )
    r_ip = p_obj.add_run("IP: 161.97.140.245")
    r_ip.bold = True
    r_ip.font.color.rgb = COLOR_PRIMARY
    p_obj.add_run(
        "), utilizando las credenciales de acceso explicadas y asignadas en clase.\n\n"
        "El estudiante deberá dominar y documentar exhaustivamente el ciclo de vida de empaquetado y entrega: "
        "creación del Dockerfile, resolución de dependencias, transferencia remota de artefactos, compilación de imágenes "
        "con versionamiento formal, ejecución con mapeo de puertos y resolución de requerimientos de actualización en caliente."
    )

    add_callout(
        "CONDICIÓN OBLIGATORIA DEL SERVICIO (VERSIÓN 1)",
        "No es necesario documentar el paso a paso de la creación del código de la aplicación. Sin embargo, es un REQUISITO INDISPENSABLE "
        "que la respuesta de la aplicación (en el navegador o cliente HTTP) presente de forma explícita y visible los "
        "NOMBRES COMPLETOS del estudiante. En la sección final del taller se solicitará una actualización de versión obligatoria.",
        alert_type="warning"
    )

    # SECTION 2
    add_section_title("2.", "Datos del Entorno y Parámetros del Servidor")
    
    tbl_server = doc.add_table(rows=5, cols=2)
    tbl_server.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_server.autofit = False
    tbl_server.columns[0].width = Inches(2.2)
    tbl_server.columns[1].width = Inches(4.7)

    server_info = [
        ("Dirección IP del Servidor:", "161.97.140.245 (Servidor Linux Ubuntu/Debian)"),
        ("Protocolo de Conexión Remota:", "SSH (Secure Shell) puerto 22 / SCP / Rsync"),
        ("Credenciales de Acceso:", "Usuario y contraseña provistos por el docente en clase"),
        ("Puerto Asignado para la App:", "Puerto individual asignado a su grupo/paralelo (ej: 5000 + ID o según lista de clase)"),
        ("Motor de Contenedores:", "Docker Engine 24.x+ con Docker CLI instalados en el servidor")
    ]
    for r_idx, (k, v) in enumerate(server_info):
        c0 = tbl_server.cell(r_idx, 0)
        c1 = tbl_server.cell(r_idx, 1)
        set_cell_background(c0, "F1F5F9")
        set_cell_margins(c0, top=70, bottom=70, left=100, right=100)
        set_cell_margins(c1, top=70, bottom=70, left=100, right=100)
        set_cell_borders(c0, "single", "single", "single", "single", HEX_BORDER, "4")
        set_cell_borders(c1, "single", "single", "single", "single", HEX_BORDER, "4")
        
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_before = Pt(0)
        p0.paragraph_format.space_after = Pt(0)
        r0 = p0.add_run(k)
        r0.bold = True
        r0.font.size = Pt(9.5)
        r0.font.color.rgb = COLOR_PRIMARY

        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_before = Pt(0)
        p1.paragraph_format.space_after = Pt(0)
        r1 = p1.add_run(v)
        r1.font.size = Pt(9.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # SECTION 3
    add_section_title("3.", "Instrucciones de Llenado para el Estudiante")
    p_inst = doc.add_paragraph()
    p_inst.paragraph_format.space_before = Pt(2)
    p_inst.paragraph_format.space_after = Pt(4)
    p_inst.add_run(
        "Para que el taller sea calificado con la máxima nota, usted debe completar cada una de las secciones siguientes:\n"
        "1. "
    )
    r_i1 = p_inst.add_run("Explicación Técnica: ")
    r_i1.bold = True
    p_inst.add_run("Describir con redacción propia qué objetivo persigue cada paso, qué decisiones de arquitectura tomó y por qué.\n2. ")
    r_i2 = p_inst.add_run("Sintaxis de Comandos: ")
    r_i2.bold = True
    p_inst.add_run("Escribir los comandos reales y exactos ejecutados en su terminal (con rutas, IPs, usuarios y tags reales).\n3. ")
    r_i3 = p_inst.add_run("Evidencia Gráfica: ")
    r_i3.bold = True
    p_inst.add_run("Pegar capturas nítidas donde se observe el usuario, el prompt de la terminal del servidor y la salida en el navegador.")

    # SECTION 4
    add_section_title("4.", "Desarrollo Paso a Paso - Versión 1 del Servicio")

    # Step 4.1
    p_step1 = doc.add_paragraph()
    p_step1.paragraph_format.space_before = Pt(8)
    p_step1.paragraph_format.space_after = Pt(2)
    r_s1 = p_step1.add_run("4.1 Selección Tecnológica y Definición de Dependencias del Proyecto")
    r_s1.bold = True
    r_s1.font.size = Pt(11)
    r_s1.font.color.rgb = COLOR_PRIMARY

    p_s1_desc = doc.add_paragraph()
    p_s1_desc.paragraph_format.space_before = Pt(0)
    p_s1_desc.paragraph_format.space_after = Pt(4)
    p_s1_desc.add_run(
        "Indique el lenguaje y framework utilizado para su servicio (ej: Python/Flask/FastAPI, Node.js/Express, Java/Spring Boot, Go, etc.). "
        "Especifique el archivo donde declaró las dependencias (requirements.txt, package.json, pom.xml) y confirme la inclusión "
        "de sus nombres completos."
    )

    add_explanation_box(
        "RESPUESTA DEL ESTUDIANTE: LENGUAJE, FRAMEWORK Y GESTIÓN DE DEPENDENCIAS",
        "Detalle el lenguaje seleccionado, la versión empleada, el archivo de dependencias creado y cómo configuró el servicio para mostrar sus nombres completos.",
        min_lines=4
    )

    add_command_box(
        "CREACIÓN O INSPECCIÓN DE ARCHIVOS DEL PROYECTO",
        "Escriba los comandos usados para estructurar el proyecto e inicializar dependencias (ej: pip freeze, npm init, touch, etc.)",
        placeholder_cmd="cat requirements.txt   # o cat package.json"
    )

    # Step 4.2
    p_step2 = doc.add_paragraph()
    p_step2.paragraph_format.space_before = Pt(8)
    p_step2.paragraph_format.space_after = Pt(2)
    r_s2 = p_step2.add_run("4.2 Creación, Configuración y Análisis del Dockerfile")
    r_s2.bold = True
    r_s2.font.size = Pt(11)
    r_s2.font.color.rgb = COLOR_PRIMARY

    p_s2_desc = doc.add_paragraph()
    p_s2_desc.paragraph_format.space_before = Pt(0)
    p_s2_desc.paragraph_format.space_after = Pt(4)
    p_s2_desc.add_run(
        "Presente el contenido íntegro de su archivo Dockerfile y analice qué función cumple cada una de las directivas principales "
        "(FROM, WORKDIR, COPY, RUN, EXPOSE, CMD/ENTRYPOINT)."
    )

    add_explanation_box(
        "RESPUESTA DEL ESTUDIANTE: ANÁLISIS DIRECTIVA POR DIRECTIVA DEL DOCKERFILE",
        "Explique detalladamente qué hace cada instrucción de su Dockerfile y por qué seleccionó esa imagen base (evitar imágenes 'latest' no controladas).",
        min_lines=6
    )

    add_command_box(
        "CONTENIDO EXACTO DEL DOCKERFILE",
        "Pegue o redacte el contenido completo de su Dockerfile",
        placeholder_cmd="cat Dockerfile"
    )

    # Step 4.3
    p_step3 = doc.add_paragraph()
    p_step3.paragraph_format.space_before = Pt(8)
    p_step3.paragraph_format.space_after = Pt(2)
    r_s3 = p_step3.add_run("4.3 Transferencia de Archivos al Servidor Remoto (161.97.140.245)")
    r_s3.bold = True
    r_s3.font.size = Pt(11)
    r_s3.font.color.rgb = COLOR_PRIMARY

    p_s3_desc = doc.add_paragraph()
    p_s3_desc.paragraph_format.space_before = Pt(0)
    p_s3_desc.paragraph_format.space_after = Pt(4)
    p_s3_desc.add_run(
        "Documente el procedimiento y comando empleado para copiar su carpeta de trabajo local hacia el servidor remoto "
        "(ej: mediante scp, rsync o clonación con Git). Posteriormente, muestre la conexión vía SSH y la verificación de que los "
        "archivos se encuentran alojados correctamente en su directorio de trabajo en el servidor."
    )

    add_explanation_box(
        "RESPUESTA DEL ESTUDIANTE: PROCEDIMIENTO DE TRANSFERENCIA Y CONEXIÓN REMOTA",
        "Explique cómo transfirió los archivos al servidor 161.97.140.245, en qué directorio del servidor los ubicó y cómo inició sesión por SSH.",
        min_lines=4
    )

    add_command_box(
        "TRANSFERENCIA DE ARCHIVOS Y ACCESO SSH",
        "Comandos exactos ejecutados en su máquina local y en el servidor remoto",
        placeholder_cmd="scp -r ./mi-proyecto usuario@161.97.140.245:/home/usuario/\nssh usuario@161.97.140.245\nls -la /home/usuario/mi-proyecto"
    )

    add_screenshot_box(
        "Archivos del Proyecto en el Servidor Remoto (161.97.140.245)",
        "La captura debe mostrar la terminal conectada por SSH al servidor con la IP visible y el listado de archivos (ls -la)."
    )

    # Step 4.4
    p_step4 = doc.add_paragraph()
    p_step4.paragraph_format.space_before = Pt(8)
    p_step4.paragraph_format.space_after = Pt(2)
    r_s4 = p_step4.add_run("4.4 Construcción de la Imagen Docker en el Servidor (Versión 1 - v1)")
    r_s4.bold = True
    r_s4.font.size = Pt(11)
    r_s4.font.color.rgb = COLOR_PRIMARY

    p_s4_desc = doc.add_paragraph()
    p_s4_desc.paragraph_format.space_before = Pt(0)
    p_s4_desc.paragraph_format.space_after = Pt(4)
    p_s4_desc.add_run(
        "Estando dentro del servidor remoto, ejecute el comando para compilar su imagen Docker asignando un nombre personalizado y la "
        "etiqueta de versión 'v1' o '1.0' (ej: nombre-app:v1). Demuestre que la imagen fue creada en el registro local del servidor."
    )

    add_explanation_box(
        "RESPUESTA DEL ESTUDIANTE: EXPLICACIÓN DE LA CONSTRUCCIÓN DE LA IMAGEN",
        "Explique qué parámetros utilizó en docker build (-t, contexto .), cómo funciona la caché de capas y qué tamaño final obtuvo la imagen.",
        min_lines=4
    )

    add_command_box(
        "CONSTRUCCIÓN Y LISTADO DE IMÁGENES DOCKER",
        "Comandos ejecutados en el servidor para compilar y comprobar la imagen v1",
        placeholder_cmd="docker build -t mi-app-estudiante:v1 .\ndocker images | grep mi-app-estudiante"
    )

    add_screenshot_box(
        "Compilación Exitosa de la Imagen v1 (docker build & docker images)",
        "Captura de pantalla de la terminal mostrando la finalización del build y la salida de 'docker images'."
    )

    # Step 4.5
    p_step5 = doc.add_paragraph()
    p_step5.paragraph_format.space_before = Pt(8)
    p_step5.paragraph_format.space_after = Pt(2)
    r_s5 = p_step5.add_run("4.5 Despliegue y Ejecución del Contenedor (Servicio v1)")
    r_s5.bold = True
    r_s5.font.size = Pt(11)
    r_s5.font.color.rgb = COLOR_PRIMARY

    p_s5_desc = doc.add_paragraph()
    p_s5_desc.paragraph_format.space_before = Pt(0)
    p_s5_desc.paragraph_format.space_after = Pt(4)
    p_s5_desc.add_run(
        "Inicie el contenedor en segundo plano (detached mode) mapeando el puerto asignado del servidor hacia el puerto interno "
        "donde escucha su aplicación. Asigne un nombre descriptivo al contenedor e inspeccione su estado con 'docker ps' y 'docker logs'."
    )

    add_explanation_box(
        "RESPUESTA DEL ESTUDIANTE: EXPLICACIÓN DE LOS PARÁMETROS DE DOCKER RUN",
        "Justifique cada bandera utilizada (-d, -p puerto_host:puerto_contenedor, --name, --restart unless-stopped) y qué puerto seleccionó.",
        min_lines=4
    )

    add_command_box(
        "DESPLIEGUE DEL CONTENEDOR Y REVISIÓN DE LOGS",
        "Comandos de ejecución e inspección en el servidor",
        placeholder_cmd="docker run -d -p 5001:5000 --name contenedor-v1 --restart unless-stopped mi-app-estudiante:v1\ndocker ps\ndocker logs contenedor-v1"
    )

    add_screenshot_box(
        "Contenedor v1 en Estado 'Up' e Inspección de Logs",
        "Captura de pantalla de la terminal mostrando la salida de 'docker ps' y 'docker logs' evidenciando que el servicio arrancó."
    )

    # Step 4.6
    p_step6 = doc.add_paragraph()
    p_step6.paragraph_format.space_before = Pt(8)
    p_step6.paragraph_format.space_after = Pt(2)
    r_s6 = p_step6.add_run("4.6 Verificación y Demostración del Servicio en Funcionamiento (v1)")
    r_s6.bold = True
    r_s6.font.size = Pt(11)
    r_s6.font.color.rgb = COLOR_PRIMARY

    p_s6_desc = doc.add_paragraph()
    p_s6_desc.paragraph_format.space_before = Pt(0)
    p_s6_desc.paragraph_format.space_after = Pt(4)
    p_s6_desc.add_run(
        "Acceda a su servicio desde una computadora cliente ingresando a la URL pública del servidor con el puerto mapeado "
        "(http://161.97.140.245:PUERTO) o mediante curl. Verifique que la respuesta contenga sus NOMBRES COMPLETOS."
    )

    add_explanation_box(
        "RESPUESTA DEL ESTUDIANTE: VALIDACIÓN DEL ACCESO AL SERVICIO v1",
        "Indique la URL exacta utilizada, el método de prueba (navegador web o curl) y el código de estado HTTP recibido (200 OK).",
        min_lines=3
    )

    add_command_box(
        "PRUEBA DE CONECTIVIDAD Y RESPUESTA HTTP",
        "Comando curl ejecutado localmente o en el servidor para validar respuesta",
        placeholder_cmd="curl -i http://161.97.140.245:5001"
    )

    add_screenshot_box(
        "Navegador Web / Cliente HTTP mostrando Servicio v1 con Nombres Completos",
        "La captura debe mostrar claramente la barra de direcciones del navegador con la IP 161.97.140.245:PUERTO y sus NOMBRES COMPLETOS."
    )

    # SECTION 5 - RETO FINAL
    add_section_title("5.", "Reto Evaluatorio Obligatorio: Versionamiento y Actualización (v2)")

    add_callout(
        "ENUNCIADO DEL RETO PRÁCTICO: VERSIÓN 2 (v2)",
        "Una vez desplegada y demostrada la Versión 1, el estudiante DEBE aplicar un cambio en el código fuente de la aplicación "
        "para incorporar de manera obligatoria y destacada el mensaje institucional:\n\n"
        "                     👉  \"Yo estudio en Yavirac\"  👈\n\n"
        "(Conservando además sus Nombres Completos). A continuación, deberá generar una NUEVA VERSIÓN DE LA IMAGEN DOCKER "
        "etiquetada con la versión 2 (ej: :v2 o :2.0) y desplegar un NUEVO SERVICIO / CONTENEDOR actualizado en el servidor 161.97.140.245.",
        alert_type="warning"
    )

    p_r_desc = doc.add_paragraph()
    p_r_desc.paragraph_format.space_before = Pt(4)
    p_r_desc.paragraph_format.space_after = Pt(4)
    p_r_desc.add_run(
        "Este ejercicio simula un despliegue continuo en entornos de producción: cómo actualizar un servicio sin perder el control "
        "de versiones previas, cómo manejar el contenedor anterior y cómo verificar el despliegue del nuevo release."
    )

    # 5.1
    p_r1 = doc.add_paragraph()
    p_r1.paragraph_format.space_before = Pt(6)
    p_r1.paragraph_format.space_after = Pt(2)
    r_r1 = p_r1.add_run("5.1 Explicación del Cambio Realizado en el Código Fuente")
    r_r1.bold = True
    r_r1.font.size = Pt(10.5)
    r_r1.font.color.rgb = COLOR_PRIMARY

    add_explanation_box(
        "RESPUESTA DEL ESTUDIANTE: MODIFICACIÓN EN EL CÓDIGO",
        "Explique qué archivo modificó (ej: app.py, index.js), cómo integró el mensaje 'Yo estudio en Yavirac' y cómo mantuvo sus nombres completos.",
        min_lines=4
    )

    # 5.2
    p_r2 = doc.add_paragraph()
    p_r2.paragraph_format.space_before = Pt(6)
    p_r2.paragraph_format.space_after = Pt(2)
    r_r2 = p_r2.add_run("5.2 Transferencia o Modificación de Archivos y Construcción de la Imagen v2")
    r_r2.bold = True
    r_r2.font.size = Pt(10.5)
    r_r2.font.color.rgb = COLOR_PRIMARY

    add_explanation_box(
        "RESPUESTA DEL ESTUDIANTE: ESTRATEGIA DE ACTUALIZACIÓN DE ARTEFACTOS Y BUILD v2",
        "¿Editó directamente en el servidor (con nano/vim) o volvió a transferir los cambios con scp/git? Justifique y explique la construcción del tag v2.",
        min_lines=4
    )

    add_command_box(
        "CONSTRUCCIÓN DE LA IMAGEN CON TAG v2",
        "Comandos ejecutados en el servidor para construir la imagen v2 y listar ambas versiones",
        placeholder_cmd="docker build -t mi-app-estudiante:v2 .\ndocker images | grep mi-app-estudiante"
    )

    add_screenshot_box(
        "Registro Local del Servidor mostrando ambas Imágenes (:v1 y :v2)",
        "Captura de la terminal donde se visualicen claramente ambas imágenes coexistiendo en 'docker images'."
    )

    # 5.3
    p_r3 = doc.add_paragraph()
    p_r3.paragraph_format.space_before = Pt(6)
    p_r3.paragraph_format.space_after = Pt(2)
    r_r3 = p_r3.add_run("5.3 Estrategia de Reemplazo y Despliegue del Nuevo Contenedor v2")
    r_r3.bold = True
    r_r3.font.size = Pt(10.5)
    r_r3.font.color.rgb = COLOR_PRIMARY

    add_explanation_box(
        "RESPUESTA DEL ESTUDIANTE: GESTIÓN DEL CONTENEDOR PREVIO Y DESPLIEGUE v2",
        "Explique qué hizo con el contenedor v1 (¿lo detuvo con docker stop y eliminó con docker rm para liberar el puerto, o levantó v2 en un puerto alternativo?) y cómo desplegó el nuevo servicio.",
        min_lines=5
    )

    add_command_box(
        "COMANDOS DE DETENCIÓN, ELIMINACIÓN Y DESPLIEGUE DEL SERVICIO v2",
        "Comandos exactos ejecutados para hacer la transición hacia la versión 2",
        placeholder_cmd="docker stop contenedor-v1\ndocker rm contenedor-v1\ndocker run -d -p 5001:5000 --name contenedor-v2 --restart unless-stopped mi-app-estudiante:v2\ndocker ps"
    )

    # 5.4
    p_r4 = doc.add_paragraph()
    p_r4.paragraph_format.space_before = Pt(6)
    p_r4.paragraph_format.space_after = Pt(2)
    r_r4 = p_r4.add_run("5.4 Verificación Final del Servicio v2 en Navegador / Cliente HTTP")
    r_r4.bold = True
    r_r4.font.size = Pt(10.5)
    r_r4.font.color.rgb = COLOR_PRIMARY

    add_command_box(
        "PRUEBA HTTP FINAL DE LA VERSIÓN 2",
        "Comando curl ejecutado para verificar el nuevo contenido retornado",
        placeholder_cmd="curl http://161.97.140.245:5001"
    )

    add_screenshot_box(
        "Servicio v2 en Producción mostrando: 'Yo estudio en Yavirac' + Nombres Completos",
        "Captura obligatoria del navegador web o curl mostrando la IP 161.97.140.245, el mensaje 'Yo estudio en Yavirac' y sus nombres completos."
    )

    # SECTION 6 - CUESTIONARIO TÉCNICO
    add_section_title("6.", "Cuestionario de Fundamentación y Análisis Técnico")

    p_q_intro = doc.add_paragraph()
    p_q_intro.paragraph_format.space_before = Pt(2)
    p_q_intro.paragraph_format.space_after = Pt(4)
    p_q_intro.add_run("Responda de forma clara, técnica y concisa las siguientes preguntas formuladas a partir de la práctica realizada:")

    questions = [
        ("Pregunta 1: Diferencia y Mapeo de Puertos (-p Host:Contenedor)",
         "En el comando docker run -p 8080:5000, ¿cuál es la diferencia entre el puerto 8080 y el puerto 5000? ¿Qué sucedería si dos estudiantes intentan desplegar mapeando al mismo puerto 8080 en el servidor 161.97.140.245?"),
        
        ("Pregunta 2: Buenas Prácticas de Versionamiento de Imágenes Docker",
         "¿Por qué en entornos de producción empresariales se desaconseja rotundamente utilizar el tag ':latest' y cómo el etiquetado semántico (:v1, :v2) facilita tareas de auditoría y rollback (regreso a versión estable anterior)?"),

        ("Pregunta 3: Persistencia y Políticas de Reinicio Automático",
         "¿Qué efecto tiene el parámetro '--restart unless-stopped' o '--restart always' si el administrador del servidor 161.97.140.245 reinicia la máquina física/virtual? ¿Qué pasaría con un contenedor ejecutado sin ese parámetro?"),

        ("Pregunta 4: Ventajas de la Contenedorización frente al Despliegue Tradicional",
         "A partir de su experiencia en este taller, ¿qué beneficios aportó Docker en comparación con tener que instalar manualmente en el servidor el intérprete de Python/Node/Java, sus gestores de paquetes y librerías?")
    ]

    for q_title, q_text in questions:
        add_explanation_box(q_title, q_text, min_lines=4)

    # SECTION 7 - CONCLUSIONES
    add_section_title("7.", "Conclusiones y Recomendaciones del Estudiante")
    add_explanation_box(
        "CONCLUSIONES PERSONALES DE LA PRÁCTICA (MÍNIMO 2)",
        "Redacte al menos dos conclusiones técnicas sólidas sobre el aprendizaje alcanzado al empaquetar y desplegar servicios en un servidor real con Docker.",
        min_lines=4
    )
    add_explanation_box(
        "RECOMENDACIONES TÉCNICAS (MÍNIMO 2)",
        "Proponga dos recomendaciones o precauciones que otros desarrolladores deben tener en cuenta al gestionar puertos, imágenes o seguridad en Docker.",
        min_lines=4
    )

    # SECTION 8 - RÚBRICA
    add_section_title("8.", "Rúbrica de Evaluación del Taller")

    tbl_rubric = doc.add_table(rows=7, cols=4)
    tbl_rubric.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_rubric.autofit = False

    r_widths = [Inches(1.8), Inches(3.2), Inches(0.9), Inches(1.0)]
    for row in tbl_rubric.rows:
        for idx, w in enumerate(r_widths):
            row.cells[idx].width = w

    rubric_headers = ["CRITERIO EVALUADO", "DESCRIPCIÓN DEL DESEMPEÑO ESPERADO", "PUNTAJE", "NOTA OBT."]
    for idx, text in enumerate(rubric_headers):
        c = tbl_rubric.cell(0, idx)
        set_cell_background(c, HEX_PRIMARY)
        set_cell_margins(c, top=80, bottom=80, left=80, right=80)
        set_cell_borders(c, "single", "single", "single", "single", HEX_PRIMARY, "6")
        p = c.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(text)
        r.bold = True
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(255, 255, 255)

    rubric_rows = [
        ("1. Dockerfile y Dependencias",
         "Estructuración adecuada del proyecto, selección de imagen base óptima y explicación clara de cada directiva en el Dockerfile.",
         "2.00 pts"),
        ("2. Transferencia y Conexión SSH",
         "Uso correcto de comandos (scp, rsync, git) para llevar los artefactos al servidor 161.97.140.245 y verificación vía SSH.",
         "1.50 pts"),
        ("3. Despliegue y Servicio v1",
         "Construcción de imagen v1, ejecución del contenedor mapeando puertos y evidencia del servicio activo mostrando los nombres completos.",
         "2.50 pts"),
        ("4. Reto de Actualización (v2)",
         "Modificación correcta del código incorporando 'Yo estudio en Yavirac', construcción de imagen :v2 y despliegue del nuevo servicio con evidencia.",
         "2.50 pts"),
        ("5. Cuestionario Técnico y Conclusiones",
         "Respuestas fundamentadas a las preguntas técnicas, explicación rigurosa de comandos y conclusiones pertinentes.",
         "1.50 pts"),
        ("TOTAL EVALUACIÓN",
         "Cumplimiento integral de todos los parámetros técnicos y documentales del taller práctico.",
         "10.00 pts")
    ]

    for r_idx, (crit, desc, pts) in enumerate(rubric_rows, start=1):
        c0 = tbl_rubric.cell(r_idx, 0)
        c1 = tbl_rubric.cell(r_idx, 1)
        c2 = tbl_rubric.cell(r_idx, 2)
        c3 = tbl_rubric.cell(r_idx, 3)

        is_total = (r_idx == len(rubric_rows))
        bg = "E2E8F0" if is_total else ("F8FAFC" if r_idx % 2 == 0 else "FFFFFF")

        for c in [c0, c1, c2, c3]:
            set_cell_background(c, bg)
            set_cell_margins(c, top=60, bottom=60, left=80, right=80)
            set_cell_borders(c, "single", "single", "single", "single", HEX_BORDER, "4")

        # Crit
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_before = Pt(0)
        p0.paragraph_format.space_after = Pt(0)
        r0 = p0.add_run(crit)
        r0.bold = True
        r0.font.size = Pt(8.5)
        if is_total:
            r0.font.color.rgb = COLOR_PRIMARY

        # Desc
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_before = Pt(0)
        p1.paragraph_format.space_after = Pt(0)
        r1 = p1.add_run(desc)
        r1.font.size = Pt(8.5)

        # Pts
        p2 = c2.paragraphs[0]
        p2.paragraph_format.space_before = Pt(0)
        p2.paragraph_format.space_after = Pt(0)
        p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r2 = p2.add_run(pts)
        r2.bold = True
        r2.font.size = Pt(8.5)

        # Nota
        p3 = c3.paragraphs[0]
        p3.paragraph_format.space_before = Pt(0)
        p3.paragraph_format.space_after = Pt(0)
        p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r3 = p3.add_run("____" if not is_total else "____ / 10")
        r3.bold = is_total
        r3.font.size = Pt(8.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # Output file
    output_path = r"d:\YAVIRAC\tendencias\Taller_Practico_Docker_Servidor_Remoto.docx"
    doc.save(output_path)
    print(f"Documento Word guardado exitosamente en: {output_path}")

if __name__ == "__main__":
    create_workshop_doc()
