<?php
/* Smarty version 3.1.48, created on 2024-11-27 19:26:42
  from '/var/www/html/themes/classic/templates/cms/category.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.48',
  'unifunc' => 'content_6747646290a909_13440755',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '7608ec7a4131e20ab69bde820a745daac6e68c5a' => 
    array (
      0 => '/var/www/html/themes/classic/templates/cms/category.tpl',
      1 => 1702485415,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_6747646290a909_13440755 (Smarty_Internal_Template $_smarty_tpl) {
$_smarty_tpl->_loadInheritance();
$_smarty_tpl->inheritance->init($_smarty_tpl, true);
?>


<?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_576764055674764629026d7_48344730', 'page_title');
?>


<?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_464067927674764629036f0_64218481', 'page_content');
?>

<?php $_smarty_tpl->inheritance->endChild($_smarty_tpl, 'page.tpl');
}
/* {block 'page_title'} */
class Block_576764055674764629026d7_48344730 extends Smarty_Internal_Block
{
public $subBlocks = array (
  'page_title' => 
  array (
    0 => 'Block_576764055674764629026d7_48344730',
  ),
);
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>

  <?php echo htmlspecialchars($_smarty_tpl->tpl_vars['cms_category']->value['name'], ENT_QUOTES, 'UTF-8');?>

<?php
}
}
/* {/block 'page_title'} */
/* {block 'cms_sub_categories'} */
class Block_51303087767476462903b19_07497522 extends Smarty_Internal_Block
{
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>

    <?php if ($_smarty_tpl->tpl_vars['sub_categories']->value) {?>
      <p><?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'List of sub categories in %name%:','d'=>'Shop.Theme.Global','sprintf'=>array('%name%'=>$_smarty_tpl->tpl_vars['cms_category']->value['name'])),$_smarty_tpl ) );?>
</p>
      <ul>
        <?php
$_from = $_smarty_tpl->smarty->ext->_foreach->init($_smarty_tpl, $_smarty_tpl->tpl_vars['sub_categories']->value, 'sub_category');
$_smarty_tpl->tpl_vars['sub_category']->do_else = true;
if ($_from !== null) foreach ($_from as $_smarty_tpl->tpl_vars['sub_category']->value) {
$_smarty_tpl->tpl_vars['sub_category']->do_else = false;
?>
          <li><a href="<?php echo htmlspecialchars($_smarty_tpl->tpl_vars['sub_category']->value['link'], ENT_QUOTES, 'UTF-8');?>
"><?php echo htmlspecialchars($_smarty_tpl->tpl_vars['sub_category']->value['name'], ENT_QUOTES, 'UTF-8');?>
</a></li>
        <?php
}
$_smarty_tpl->smarty->ext->_foreach->restore($_smarty_tpl, 1);?>
      </ul>
    <?php }?>
  <?php
}
}
/* {/block 'cms_sub_categories'} */
/* {block 'cms_sub_pages'} */
class Block_177973702167476462907581_83519672 extends Smarty_Internal_Block
{
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>

    <?php if ($_smarty_tpl->tpl_vars['cms_pages']->value) {?>
      <p><?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'List of pages in %category_name%:','d'=>'Shop.Theme.Global','sprintf'=>array('%category_name%'=>$_smarty_tpl->tpl_vars['cms_category']->value['name'])),$_smarty_tpl ) );?>
</p>
      <ul>
        <?php
$_from = $_smarty_tpl->smarty->ext->_foreach->init($_smarty_tpl, $_smarty_tpl->tpl_vars['cms_pages']->value, 'cms_page');
$_smarty_tpl->tpl_vars['cms_page']->do_else = true;
if ($_from !== null) foreach ($_from as $_smarty_tpl->tpl_vars['cms_page']->value) {
$_smarty_tpl->tpl_vars['cms_page']->do_else = false;
?>
          <li><a href="<?php echo htmlspecialchars($_smarty_tpl->tpl_vars['cms_page']->value['link'], ENT_QUOTES, 'UTF-8');?>
"><?php echo htmlspecialchars($_smarty_tpl->tpl_vars['cms_page']->value['meta_title'], ENT_QUOTES, 'UTF-8');?>
</a></li>
        <?php
}
$_smarty_tpl->smarty->ext->_foreach->restore($_smarty_tpl, 1);?>
      </ul>
    <?php }?>
  <?php
}
}
/* {/block 'cms_sub_pages'} */
/* {block 'page_content'} */
class Block_464067927674764629036f0_64218481 extends Smarty_Internal_Block
{
public $subBlocks = array (
  'page_content' => 
  array (
    0 => 'Block_464067927674764629036f0_64218481',
  ),
  'cms_sub_categories' => 
  array (
    0 => 'Block_51303087767476462903b19_07497522',
  ),
  'cms_sub_pages' => 
  array (
    0 => 'Block_177973702167476462907581_83519672',
  ),
);
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>

  <?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_51303087767476462903b19_07497522', 'cms_sub_categories', $this->tplIndex);
?>


  <?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_177973702167476462907581_83519672', 'cms_sub_pages', $this->tplIndex);
?>

<?php
}
}
/* {/block 'page_content'} */
}
