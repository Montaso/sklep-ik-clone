<?php
/* Smarty version 3.1.48, created on 2024-11-27 19:27:08
  from '/var/www/html/admin/themes/default/template/controllers/carriers/helpers/form/form.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.48',
  'unifunc' => 'content_6747647c7d6303_37684284',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '16ccd5f3cc341f506beeedd868c2b70e6fb1247a' => 
    array (
      0 => '/var/www/html/admin/themes/default/template/controllers/carriers/helpers/form/form.tpl',
      1 => 1702485415,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_6747647c7d6303_37684284 (Smarty_Internal_Template $_smarty_tpl) {
$_smarty_tpl->_loadInheritance();
$_smarty_tpl->inheritance->init($_smarty_tpl, true);
?>


<?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_17532672086747647c7d1539_59745517', 'script');
?>


<?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_20107784916747647c7d2174_98725697', "label");
?>


<?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_4868274286747647c7d41b8_74192501', "field");
?>

<?php $_smarty_tpl->inheritance->endChild($_smarty_tpl, "helpers/form/form.tpl");
}
/* {block 'script'} */
class Block_17532672086747647c7d1539_59745517 extends Smarty_Internal_Block
{
public $subBlocks = array (
  'script' => 
  array (
    0 => 'Block_17532672086747647c7d1539_59745517',
  ),
);
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>

	// At the loading
	($("input[name='is_free']:checked").val() == 0) ? $('#shipping_costs_div').show('toggle'): $('#shipping_costs_div').hide();

	$(document).on('change', "input[name='is_free']", function() {
		($("input[name='is_free']:checked").val() == 0) ? $('#shipping_costs_div').show('toggle'): $('#shipping_costs_div').hide();
	});
<?php
}
}
/* {/block 'script'} */
/* {block "label"} */
class Block_20107784916747647c7d2174_98725697 extends Smarty_Internal_Block
{
public $subBlocks = array (
  'label' => 
  array (
    0 => 'Block_20107784916747647c7d2174_98725697',
  ),
);
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>

	<?php if ($_smarty_tpl->tpl_vars['input']->value['type'] == 'select' && $_smarty_tpl->tpl_vars['input']->value['name'] == 'id_tax_rules_group') {?>
		<div id="shipping_costs_div" style="display:<?php if ((isset($_smarty_tpl->tpl_vars['fields_value']->value['is_free'])) && $_smarty_tpl->tpl_vars['fields_value']->value['is_free']) {?>none<?php } else { ?>block<?php }?>">
	<?php }?>
	<?php 
$_smarty_tpl->inheritance->callParent($_smarty_tpl, $this, '{$smarty.block.parent}');
?>

<?php
}
}
/* {/block "label"} */
/* {block "field"} */
class Block_4868274286747647c7d41b8_74192501 extends Smarty_Internal_Block
{
public $subBlocks = array (
  'field' => 
  array (
    0 => 'Block_4868274286747647c7d41b8_74192501',
  ),
);
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>

	<?php 
$_smarty_tpl->inheritance->callParent($_smarty_tpl, $this, '{$smarty.block.parent}');
?>

	<?php if ($_smarty_tpl->tpl_vars['input']->value['type'] == 'select' && $_smarty_tpl->tpl_vars['input']->value['name'] == 'range_behavior') {?>
		</div>
	<?php }
}
}
/* {/block "field"} */
}
